import sqlite3
conn = None

try:
    conn = sqlite3.connect("../db/lesson.db")
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    # Task 1: Complex JOINs with Aggregation

    cursor.execute(
        """
        SELECT
            orders.order_id,
            ROUND(
                SUM(products.price * line_items.quantity),
                2
            ) AS total_price
        FROM orders
        JOIN line_items
            ON orders.order_id = line_items.order_id
        JOIN products
            ON line_items.product_id = products.product_id
        GROUP BY orders.order_id
        ORDER BY orders.order_id
        LIMIT 5
        """
    )
    order_totals = cursor.fetchall()

    print("First five order totals:")
    for row in order_totals:
        print(row)

    # Task 2: Understanding Subqueries

    cursor.execute(
        """
        SELECT
            customers.customer_name,
            ROUND(
                AVG(order_totals.total_price),
                2
            ) AS average_total_price
        FROM customers
        LEFT JOIN (
            SELECT
                orders.customer_id AS customer_id_b,
                orders.order_id,
                SUM(products.price * line_items.quantity) AS total_price
            FROM orders
            JOIN line_items
                ON orders.order_id = line_items.order_id
            JOIN products
                ON line_items.product_id = products.product_id
            GROUP BY
                orders.order_id,
                orders.customer_id
        ) AS order_totals
            ON customers.customer_id = order_totals.customer_id_b
        GROUP BY
            customers.customer_id,
            customers.customer_name
        ORDER BY customers.customer_name
        """
    )
    customer_averages = cursor.fetchall()

    print("\nAverage order price for each customer!")
    for row in customer_averages:
        print(row)

    # Task 3: Insert Transaction Based on Data

    try:
        conn.execute("BEGIN")
        cursor.execute(
            """
            SELECT customer_id
            FROM customers
            WHERE customer_name = ?
            """,
            ("Perez and Sons",),
        )
        customer_id = cursor.fetchone()[0]

        cursor.execute(
            """
            SELECT employee_id
            FROM employees
            WHERE first_name = ?
                AND last_name = ?
            """,
            ("Miranda", "Harris"),
        )
        employee_id = cursor.fetchone()[0]

        cursor.execute(
            """
            SELECT product_id
            FROM products
            ORDER BY price ASC, product_id ASC
            LIMIT 5
            """
        )
        product_rows = cursor.fetchall()
        product_ids = [row[0] for row in product_rows]

    

        cursor.execute(
            """
            INSERT INTO orders (
            customer_id,
            employee_id,
            date
            )
            VALUES (?, ?, DATE('now'))
            RETURNING order_id
            """,
            (customer_id, employee_id),
        )
        new_order_id = cursor.fetchone()[0]

        line_items_to_add = [
            (new_order_id, product_id, 10)
            for product_id in product_ids
        ]

        cursor.executemany(
            """
            INSERT INTO line_items (
                order_id,
                product_id,
                quantity
            )
            VALUES (?, ?, ?)
            """,
            line_items_to_add,
        )
        

        cursor.execute(
            """
            SELECT
                line_items.line_item_id,
                line_items.quantity,
                products.product_name
            FROM line_items
            JOIN products
                ON line_items.product_id = products.product_id
            WHERE line_items.order_id = ?
            ORDER BY line_items.line_item_id
            """,
            (new_order_id,),
        )
        new_order_items = cursor.fetchall()
        print("\nNew order line items:")
        for row in new_order_items:
            print(row)
        conn.commit()

    except sqlite3.Error:
        conn.rollback()
        raise

    # Task 4: Aggregation with HAVING

    cursor.execute(
        """
        SELECT
            employees.employee_id,
            employees.first_name,
            employees.last_name,
            COUNT(orders.order_id) AS order_count
        FROM employees
        JOIN orders
            ON employees.employee_id = orders.employee_id
        GROUP BY
            employees.employee_id,
            employees.first_name,
            employees.last_name
        HAVING COUNT(orders.order_id) > 5
        ORDER BY order_count DESC
        """
    )
    employee_order_counts = cursor.fetchall()

    print("\nEmployees associated with more than five orders:")

    for row in employee_order_counts:
        print(row)

except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if conn:
        conn.close()
        print("Database connection closed.")

            
        