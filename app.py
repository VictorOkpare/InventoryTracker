"""
app.py - FastAPI entry point for the Inventory Tracker application.

Exposes RESTful API endpoints for managing inventory items.
Replaces the original CLI script with a fully accessible web API.

Lab 4 - Re-engineering & Migration
"""

from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from models import InventoryItem, InventoryItemResponse
from controllers import (
    get_all_items,
    get_item_by_id,
    add_item,
    delete_item,
    get_summary
)
from database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize the database on application startup."""
    print("[APP] Starting Inventory Tracker API...")
    init_db()
    yield
    print("[APP] Shutting down.")


app = FastAPI(
    title="Inventory Tracker API",
    description="A RESTful API for managing inventory items. Lab 4 - Re-engineering & Migration.",
    version="2.0.0",
    lifespan=lifespan
)


@app.get("/", tags=["Root"])
def root():
    """Health check endpoint."""
    return {"message": "Inventory Tracker API is running.", "version": "2.0.0"}


@app.get("/items", response_model=list[InventoryItemResponse], tags=["Inventory"])
def list_items():
    """
    Retrieve all inventory items from the database.

    Returns:
        List of all inventory items with computed values.
    """
    return get_all_items()


@app.get("/items/{item_id}", response_model=InventoryItemResponse, tags=["Inventory"])
def get_item(item_id: int):
    """
    Retrieve a single inventory item by ID.

    Args:
        item_id: The database ID of the item.

    Returns:
        The matching inventory item or 404 if not found.
    """
    item = get_item_by_id(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail=f"Item with ID {item_id} not found.")
    return item


@app.post("/items", response_model=InventoryItemResponse, status_code=201, tags=["Inventory"])
def create_item(item: InventoryItem):
    """
    Add a new inventory item to the database.

    Args:
        item: InventoryItem with item_name, quantity, and price.

    Returns:
        The newly created item with its assigned ID and computed value.
    """
    return add_item(item)


@app.delete("/items/{item_id}", tags=["Inventory"])
def remove_item(item_id: int):
    """
    Delete an inventory item by ID.

    Args:
        item_id: The database ID of the item to delete.

    Returns:
        Confirmation message or 404 if not found.
    """
    success = delete_item(item_id)
    if not success:
        raise HTTPException(status_code=404, detail=f"Item with ID {item_id} not found.")
    return {"message": f"Item {item_id} deleted successfully."}


@app.get("/summary", tags=["Statistics"])
def inventory_summary():
    """
    Get inventory summary statistics.

    Returns:
        Highest stock item, lowest stock item, and total stock value.
    """
    return get_summary()