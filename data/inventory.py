"""
inventory.py - Data module for the Inventory Tracker application.

Contains a list of inventory items, each with item_name, quantity, and price.

Maintenance History:
    v1.0 - Initial inventory data module
"""

# --- Inventory Data ---
inventory: list[dict] = [
    {"item_name": "Laptop",     "quantity": 10, "price": 999.99},
    {"item_name": "Mouse",      "quantity": 50, "price": 25.49},
    {"item_name": "Keyboard",   "quantity": 30, "price": 45.00},
    {"item_name": "Monitor",    "quantity": 15, "price": 299.99},
    {"item_name": "USB Hub",    "quantity": 0,  "price": 19.99},
]
