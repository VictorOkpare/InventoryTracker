"""
helpers.py - Utility functions for the Inventory Tracker application.

Provides helper functions to compute statistics on inventory items.
All functions handle empty input gracefully.

Maintenance History:
    v1.0 - Initial helpers: highest_stock_item, lowest_stock_item, total_stock_value
"""


def highest_stock_item(items: list[dict]) -> dict | None:
    """
    Return the item with the highest quantity in stock.

    Args:
        items: List of inventory dicts with 'item_name', 'quantity', 'price'.

    Returns:
        The item dict with the highest quantity, or None if list is empty.
    """
    if not items:
        return None
    return max(items, key=lambda i: i["quantity"])


def lowest_stock_item(items: list[dict]) -> dict | None:
    """
    Return the item with the lowest quantity in stock.

    Args:
        items: List of inventory dicts with 'item_name', 'quantity', 'price'.

    Returns:
        The item dict with the lowest quantity, or None if list is empty.
    """
    if not items:
        return None
    return min(items, key=lambda i: i["quantity"])


def total_stock_value(items: list[dict]) -> float:
    """
    Calculate the total stock value (quantity * price) for all items.

    Args:
        items: List of inventory dicts with 'quantity' and 'price' keys.

    Returns:
        Total stock value as a float, or 0.0 if the list is empty.
    """
    if not items:
        return 0.0
    # Corrective: skip items with negative quantity or price to avoid bad totals
    return sum(
        i["quantity"] * i["price"]
        for i in items
        if i["quantity"] >= 0 and i["price"] >= 0
    )
