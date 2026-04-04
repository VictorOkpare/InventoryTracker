"""
app.py - Main entry point for the Inventory Tracker application.

Reads from inventory.py and calculates total stock value,
highest/lowest stock items, and displays a formatted table.

Maintenance History:
    v1.0 - Initial script
"""

from data.inventory import inventory
from utils.helpers import highest_stock_item, lowest_stock_item, total_stock_value


def display_inventory(items: list[dict]) -> None:
    """Print a formatted table of inventory items."""
    if not items:
        print("No inventory records available.")
        return

    print(f"\n{'='*55}")
    print(f"{'Item':<20} {'Quantity':>10} {'Price':>10} {'Value':>12}")
    print(f"{'-'*55}")
    for item in items:
        value = item["quantity"] * item["price"]
        print(f"{item['item_name']:<20} {item['quantity']:>10} {item['price']:>10.2f} {value:>12.2f}")
    print(f"{'='*55}\n")


def print_summary(items: list[dict]) -> None:
    """Compute and print inventory summary statistics."""
    if not items:
        print("No records to summarise.")
        return

    highest = highest_stock_item(items)
    lowest  = lowest_stock_item(items)
    total   = total_stock_value(items)

    print(f"{'='*55}")
    print(f"  INVENTORY SUMMARY")
    print(f"{'-'*55}")
    print(f"  Highest Stock : {highest['item_name']} (qty: {highest['quantity']})")
    print(f"  Lowest Stock  : {lowest['item_name']}  (qty: {lowest['quantity']})")
    print(f"  Total Value   : ${total:,.2f}")
    print(f"{'='*55}\n")


def main() -> None:
    """Run the Inventory Tracker demo application."""
    print("\n  INVENTORY TRACKER APPLICATION  ")

    if not inventory:
        print("No inventory records found. Exiting.")
        return

    display_inventory(inventory)
    print_summary(inventory)


if __name__ == "__main__":
    main()
