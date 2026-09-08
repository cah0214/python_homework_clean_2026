# Task 1: Reviewed robots.txt. 
# The general rule only disallows/staff/, 
# The assigned search-results page is not within that restricted path.
#
# Task 2: HTML and DOM selectors
# Search-result entry:
# Tag: li
# Classes: row cp-search-result-item
# CSS selector: li.row.cp-search-result-item
#
# Book Title:
# Tag: span
# Classes: title-content
# CSS selector: span.title-content
#
# Book author:
# Tag: a
# Class: author-link
# CSS selector: a.author-link
# 
#
# Format and publication year container:
# Tag: div
# Class: cp-format-info
# CSS selector: div.cp-format-info
# 
# Format and publication year:
# Tag: span
# Class: display-info-primary
# CSS selector: span.display-info-primary 


# Task 3: Write a Program to Extract Book Data

import json
import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

try:
    driver.get(url)
    print("Page title:", driver.title)

    book_entries = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "li.row.cp-search-result-item")

        )
    )

    print("Number of book results:", len(book_entries))

    results = []

    for entry in book_entries:
        title_element = entry.find_element(
            By.CSS_SELECTOR, "span.title-content"
        )
        title = title_element.text.strip()
        print("Title:", title)

        author_elements = entry.find_elements(
            By.CSS_SELECTOR, 'a[data-key="author-link"]'
        )

        author_names = []

        for author_element in author_elements:
            author_name = author_element.text.strip()

            if author_name:
                author_names.append(author_name)

        authors = "; ".join(author_names)
        print("Authors:", authors)

        format_div = entry.find_element(
            By.CSS_SELECTOR, "div.cp-format-info"
        )
        format_year_element = format_div.find_element(
            By.CSS_SELECTOR, "span.display-info-primary"
        )

        format_year = format_year_element.text.replace("|n", "").strip()
        print("Format-Year:", format_year)

        book_data = {
            "Title": title,
            "Authors": authors,
            "Format-Year": format_year
        }
        results.append(book_data)
    books_df = pd.DataFrame(results)

    print("\nBooks DataFrame:")
    print(books_df)

    #Task 4: Write the data to CSV and JSON
    books_df.to_csv(
        "get_books.csv",
        index=False,
    )

    with open("get_books.json", "w", encoding="utf-8") as json_file:
        json.dump(
            results,
            json_file,
            indent=4,
            ensure_ascii=False
        )
    print("\nSaved get_books.csv and get_books.json")

finally:
    driver.quit()