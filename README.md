# Inventory Tracker

## Overview

A modular Python application that tracks inventory items and computes stock statistics.

## Project Structure

```
inventoryTracker/
│
├── app.py              # Main entry point; displays inventory table and summary
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation
├── .gitignore          # Files ignored by Git
│
├── data/
│   └── inventory.py    # Inventory dataset (item_name, quantity, price)
│
└── utils/
    └── helpers.py      # Helper functions: highest/lowest stock, total value
```

## How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

## Example Output

```
  INVENTORY TRACKER APPLICATION

=======================================================
Item                   Quantity      Price        Value
-------------------------------------------------------
Laptop                       10     999.99     9999.90
Mouse                        50      25.49     1274.50
...
=======================================================

  INVENTORY SUMMARY
-------------------------------------------------------
  Highest Stock : Mouse (qty: 50)
  Lowest Stock  : USB Hub (qty: 0)
  Total Value   : $13,024.35
=======================================================
```
