"""
inventory.py - Data module for the Inventory Tracker application.

Contains a list of inventory items, each with item_name, quantity, and price.

Maintenance History:
    v1.0 - Initial inventory data module
    v1.1 - Adaptive: added add_item() with type hints and input validation (Python 3.12)
"""

# --- Inventory Data ---
inventory: list[dict] = [
    {"item_name": "Laptop",     "quantity": 10, "price": 999.99},
    {"item_name": "Mouse",      "quantity": 50, "price": 25.49},
    {"item_name": "Keyboard",   "quantity": 30, "price": 45.00},
    {"item_name": "Monitor",    "quantity": 15, "price": 299.99},
    {"item_name": "USB Hub",    "quantity": 0,  "price": 19.99},
]


# --- Adaptive Maintenance: add_item with type hints (Python 3.12 compatible) ---
def add_item(item_name: str, quantity: int, price: float) -> None:
    """
    Add a new item to the inventory list.

    Args:
        item_name: Name of the item.
        quantity:  Stock quantity (must be >= 0).
        price:     Unit price (must be >= 0).

    Raises:
        ValueError: If quantity or price are negative.
    """
    if quantity < 0:
        raise ValueError(f"Quantity must be >= 0, got {quantity}")
    if price < 0:
        raise ValueError(f"Price must be >= 0, got {price}")
    inventory.append({"item_name": item_name, "quantity": quantity, "price": price})
