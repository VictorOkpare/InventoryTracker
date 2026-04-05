"""
controllers.py - Business logic layer for the Inventory Tracker application.

Handles all database operations (CRUD) and statistics calculations.
Separates business logic from the API routing layer (app.py).

Lab 4 - Re-engineering & Migration
"""

import sqlite3
from models import InventoryItem, InventoryItemResponse
from utils.helpers import highest_stock_item, lowest_stock_item, total_stock_value
from database import get_connection


def get_all_items() -> list[InventoryItemResponse]:
    """
    Retrieve all inventory items from the database.

    Returns:
        List of InventoryItemResponse objects with id and computed value.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inventory")
    rows = cursor.fetchall()
    conn.close()

    return [
        InventoryItemResponse(
            id=row["id"],
            item_name=row["item_name"],
            quantity=row["quantity"],
            price=row["price"],
            value=row["quantity"] * row["price"]
        )
        for row in rows
    ]


def get_item_by_id(item_id: int) -> InventoryItemResponse | None:
    """
    Retrieve a single inventory item by its ID.

    Args:
        item_id: The database ID of the item.

    Returns:
        InventoryItemResponse if found, None otherwise.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inventory WHERE id = ?", (item_id,))
    row = cursor.fetchone()
    conn.close()

    if row is None:
        return None

    return InventoryItemResponse(
        id=row["id"],
        item_name=row["item_name"],
        quantity=row["quantity"],
        price=row["price"],
        value=row["quantity"] * row["price"]
    )


def add_item(item: InventoryItem) -> InventoryItemResponse:
    """
    Insert a new inventory item into the database.

    Args:
        item: InventoryItem with item_name, quantity, and price.

    Returns:
        InventoryItemResponse with the new item's database ID and value.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO inventory (item_name, quantity, price) VALUES (?, ?, ?)",
        (item.item_name, item.quantity, item.price)
    )
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()

    return InventoryItemResponse(
        id=new_id,
        item_name=item.item_name,
        quantity=item.quantity,
        price=item.price,
        value=item.quantity * item.price
    )


def delete_item(item_id: int) -> bool:
    """
    Delete an inventory item from the database by ID.

    Args:
        item_id: The database ID of the item to delete.

    Returns:
        True if the item was deleted, False if not found.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM inventory WHERE id = ?", (item_id,))
    conn.commit()
    deleted = cursor.rowcount > 0
    conn.close()
    return deleted


def get_summary() -> dict:
    """
    Compute and return inventory summary statistics.

    Returns:
        Dictionary with highest stock item, lowest stock item,
        and total stock value.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inventory")
    rows = [dict(row) for row in cursor.fetchall()]
    conn.close()

    if not rows:
        return {"message": "No inventory records found."}

    highest = highest_stock_item(rows)
    lowest  = lowest_stock_item(rows)
    total   = total_stock_value(rows)

    return {
        "highest_stock_item": highest["item_name"],
        "highest_quantity":   highest["quantity"],
        "lowest_stock_item":  lowest["item_name"],
        "lowest_quantity":    lowest["quantity"],
        "total_stock_value":  round(total, 2)
    }