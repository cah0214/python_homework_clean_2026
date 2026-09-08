# Task 6; Scrape the OWASP Top 10

import pandas as pd 

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

url = "https://owasp.org/Top10/2025/"

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)
try:
    driver.get(url)
    print("Page title:", driver.title)

    risk_links = driver.find_elements(
        By.XPATH,
        '//article//ol/li/a[contains(@href, "_2025-")]'
    )
    print("Number of matching links:", len(risk_links))

    owasp_results = []
    for risk_link in risk_links:
        title = risk_link.text.strip()
        href = risk_link.get_attribute("href")

        risk_data = {
            "title": title,
            "Link": href
        }
        owasp_results.append(risk_data)

    print("\nOWASP Top 10:")
    print(owasp_results)

    owasp_df = pd.DataFrame(owasp_results)

    owasp_df.to_csv(
        "owasp_top_10.csv",
        index=False)

    print("Saved owasp_top_10.csv")

finally:
    driver.quit()