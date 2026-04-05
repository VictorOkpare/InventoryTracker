"""
models.py - Pydantic data models for the Inventory Tracker application.

Defines the data schema for inventory items using Pydantic for
automatic validation, type enforcement, and serialization.

Lab 4 - Re-engineering & Migration
"""

from pydantic import BaseModel, Field


class InventoryItem(BaseModel):
    """
    Represents a single inventory item.

    Attributes:
        item_name: Name of the inventory item.
        quantity:  Number of units in stock (must be 0 or more).
        price:     Unit price in dollars (must be greater than 0).
    """
    item_name: str
    quantity: int = Field(..., ge=0, description="Units in stock, cannot be negative")
    price: float = Field(..., gt=0, description="Unit price, must be greater than zero")


class InventoryItemResponse(InventoryItem):
    """
    Extends InventoryItem to include database-assigned fields
    returned in API responses.

    Attributes:
        id:    Auto-assigned database row ID.
        value: Computed total value (quantity * price).
    """
    id: int
    value: float