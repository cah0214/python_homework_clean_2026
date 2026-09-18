# Task 5: Read SQL Data into DataFrame

import sqlite3
import pandas as pd

conn = None

try:
    conn = sqlite3.connect("../db/lesson.db")

    sql_statement = """
    SELECT
        line_items.line_item_id,
        line_items.quantity,
        line_items.product_id,
        products.product_name,
        products.price
    FROM line_items
    JOIN products ON line_items.product_id = products.product_id
    """

    df = pd.read_sql_query(sql_statement, conn)

    print("First five rows:")
    print(df.head())

    df["total"] = df["quantity"] * df["price"]

    print("\nFirst five rows with total column:")
    print(df.head())

    order_summary = df.groupby("product_id").agg({
        "line_item_id": "count",
        "total": "sum",
        "product_name": "first"
    }).reset_index()

    print("\nFirst five rows of the order summary:")
    print(order_summary.head())

    order_summary = order_summary.sort_values(
        by="product_name"
    ).reset_index(drop=True)

    print("\nSorted order summary:")
    print(order_summary.head())

    order_summary.to_csv(
        "order_summary.csv",
        index=False
    )

    print("\nSaved order_summary.csv")


except (sqlite3.Error, pd.errors.DatabaseError) as error:
    print("Database error: ", error)

finally:
    if conn:
        conn.close()
        print("Database connection closed.")