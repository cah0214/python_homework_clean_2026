# Task 1: Create a New SQLite Database 

import sqlite3
def add_publisher(cursor, name):
    try:
        cursor.execute(
            "INSERT OR IGNORE INTO publishers (name) VALUES (?)",
            (name,)
        )
    except sqlite3.Error as error:
        print("Error adding publisher: ", error)

    cursor.execute(
    "SELECT * FROM publishers WHERE name = ?",
    (name,)
    )
    return cursor.fetchone()[0]

def add_magazine(cursor, name, publisher_id):
    try:
        cursor.execute(
            "INSERT OR IGNORE INTO magazines (name, publisher_id) VALUES (?, ?)",
            (name, publisher_id)
        )

        cursor.execute(
            "SELECT * FROM magazines WHERE name = ?",
            (name,)
        )

        return cursor.fetchone()[0]

    except sqlite3.Error as error:
        print("Error adding magazine: ", error)
        return None


def add_subscriber(cursor, name, address):
    try:
        cursor.execute(
            """
            SELECT subscriber_id
            FROM subscribers
            WHERE name = ? AND address = ?
            """,
            (name, address)
        )
        existing_subscriber = cursor.fetchone()
        if existing_subscriber:
            return existing_subscriber[0]

        cursor.execute(
            "INSERT OR IGNORE INTO subscribers (name, address) VALUES (?, ?)",
            (name, address)
        )
        return cursor.lastrowid

    except sqlite3.Error as error:
        print("Error adding subscriber: ", error)
        return None

def add_subscription(
        cursor,
        subscriber_id,
        magazine_id,
        expiration_date
    ):
    try:
        cursor.execute(
            """
            INSERT OR IGNORE INTO subscriptions (
                subscriber_id,
                magazine_id,
                expiration_date
            )
            VALUES (?, ?, ?)
            """,
            (subscriber_id, magazine_id, expiration_date)
        )

        cursor.execute(
            """
            SELECT subscription_id
            FROM subscriptions
            WHERE subscriber_id = ? AND magazine_id = ?
            """,
            (subscriber_id, magazine_id)
        )

        return cursor.lastrowid

    except sqlite3.Error as error:
        print("Error adding subscription: ", error)
        return None
conn = None
try:
    conn = sqlite3.connect("../db/magazines.db")
    conn.execute("PRAGMA foreign_keys = 1;")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS publishers (
        publisher_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE
                        
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS magazines (
        magazine_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        publisher_id INTEGER NOT NULL,
        FOREIGN KEY (publisher_id)
            REFERENCES publishers (publisher_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscribers (
        subscriber_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        address TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscriptions (
        subscription_id INTEGER PRIMARY KEY,
        subscriber_id INTEGER NOT NULL,
        magazine_id INTEGER NOT NULL,
        expiration_date TEXT NOT NULL,
        FOREIGN KEY (subscriber_id)
            REFERENCES subscribers (subscriber_id),
        FOREIGN KEY (magazine_id)
            REFERENCES magazines (magazine_id),
        UNIQUE (subscriber_id, magazine_id)
    )
    """)

    publisher_1_id = add_publisher(cursor, "Tech Today")
    publisher_2_id = add_publisher(cursor, "Health Weekly")
    publisher_3_id = add_publisher(cursor, "Travel Monthly")

    magazine_1_id = add_magazine(cursor, "Tech Today", publisher_1_id)
    magazine_2_id = add_magazine(cursor, "Health Weekly", publisher_2_id)
    magazine_3_id = add_magazine(cursor, "Travel Monthly", publisher_3_id)

    subscriber_1_id = add_subscriber(cursor, "Alice Smith", "123 Main St")
    subscriber_2_id = add_subscriber(cursor, "Bob Johnson", "456 Oak Ave")
    subscriber_3_id = add_subscriber(cursor, "Charlie Brown", "789 Pine Rd")

    add_subscription(cursor, subscriber_1_id, magazine_1_id, "2024-12-31")
    add_subscription(cursor, subscriber_2_id, magazine_2_id, "2024-11-30")
    add_subscription(cursor, subscriber_3_id, magazine_3_id, "2024-10-31")

    cursor.execute("""
    SELECT *
    FROM subscribers
    """)

    subscriber_rows = cursor.fetchall()

    print("\nAll subscribers:")

    for row in subscriber_rows:
        print(row)

    cursor.execute("""
    SELECT *
    FROM magazines
    ORDER BY name ASC
    """)

    magazine_rows = cursor.fetchall()

    print("\nAll magazines (sorted by name):")

    for row in magazine_rows:
        print(row)

    cursor.execute("""
    SELECT
        magazines.magazine_id,
        magazines.name,
        publishers.name
    FROM magazines
    JOIN publishers
      ON magazines.publisher_id = publishers.publisher_id
    WHERE publishers.name = ?
    """, ("Tech Today",))

    publisher_magazine_rows = cursor.fetchall()

    print("\nMagazines published by 'Tech Today':")

    for row in publisher_magazine_rows:
        print(row)

    print("Database created and connected successfully")
    print("All four tables created successfully")
    

except sqlite3.Error as error:
    print("Database error: ", error)

finally:
    if conn:
        conn.close()
        print("Database connection closed")


