from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from database.request_inventory_db import add_item, get_inventory, remove_item, remove_item_by_id, update_item_quantity, update_item_quantity_by_id

class Item(BaseModel):
    product: str
    quantity: int
    userid: str

app = FastAPI()

@app.post("/inventory/add_item")
async def add_item_route(item: Item):
    add_item(item.product, item.quantity, item.userid)
    return {"message": "Item added to inventory"}

@app.get("/inventory/get/{user_id}")
def read_inventory(user_id: int):
    inventory = get_inventory(user_id)
    if not inventory:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return inventory

@app.delete("/inventory/remove/{user_id}/{item_name}")
def remove_item_route(user_id: str, item_name: str):
    remove_item(item_name, user_id)
    return {"message": "Item removed from inventory"}

@app.delete("/inventory/remove_by_id/{id}")
def remove_item_by_product_route(id: int):
    remove_item_by_id(id)
    return {"message": "Item removed from inventory"}

@app.put("/inventory/update_quantity/{user_id}/{item_name}/{item_quantity}")
def update_item_quantity_route(user_id: str, item_name: str, item_quantity: int):
    update_item_quantity(user_id, item_name, item_quantity)
    return {"message": "Item quantity updated"}

@app.put("/inventory/update_quantity_by_id/{id}/{item_quantity}")
def update_item_quantity_by_id_route(id: int, item_quantity: int):
    update_item_quantity_by_id(id, item_quantity)
    return {"message": "Item quantity updated"}





