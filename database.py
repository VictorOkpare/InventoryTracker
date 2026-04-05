"""
database.py - SQLite database setup and connection for Inventory Tracker.

Handles database initialization, table creation, and seeding
from the existing inventory data module.

Lab 4 - Re-engineering & Migration
"""

import sqlite3
from data.inventory import inventory

DB_PATH = "inventory.db"


def get_connection() -> sqlite3.Connection:
    """
    Create and return a new SQLite database connection.

    Returns:
        sqlite3.Connection with row_factory set for dict-like row access.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    """
    Initialize the database.

    Creates the inventory table if it does not exist,
    then seeds it with data from data/inventory.py if the table is empty.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT    NOT NULL,
            quantity  INTEGER NOT NULL CHECK(quantity >= 0),
            price     REAL    NOT NULL CHECK(price > 0)
        )
    """)
    conn.commit()

    # Seed only if table is empty
    cursor.execute("SELECT COUNT(*) FROM inventory")
    count = cursor.fetchone()[0]

    if count == 0:
        for item in inventory:
            cursor.execute(
                "INSERT INTO inventory (item_name, quantity, price) VALUES (?, ?, ?)",
                (item["item_name"], item["quantity"], item["price"])
            )
        conn.commit()
        print(f"[DB] Seeded {len(inventory)} items into inventory table.")
    else:
        print(f"[DB] Database already has {count} records. Skipping seed.")

    conn.close()