from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

import sys
sys.path.append('..')

from database.request_users_db import add_user, get_user, remove_user, update_user_email, update_user_firstname, update_user_lastname, update_user_password, get_all_users
from database.request_userhealth_db import add_userhealth, get_userhealth, remove_userhealth, update_userhealth_gender, update_userhealth_height, update_userhealth_weight, update_userhealth_age, update_userhealth_activity_level
from database.request_inventory_db import add_item, get_inventory, remove_item, remove_item_by_id, update_item_quantity, update_item_quantity_by_id, get_all_products
from recipe_api.recipe_api import get_recipes

class User(BaseModel):
    userid: str
    password: str
    firstname: str
    lastname: str
    email: str

class UserHealth(BaseModel):
    userid: str
    gender: str
    height: int
    weight: int
    age: int
    activity_level: str

class Item(BaseModel):
    product: str
    quantity: int
    userid: str

app = FastAPI()


''' -------------- USER ROUTES --------------- '''

@app.post("/users/add_user")
async def add_user_route(user: User):
    print(user)
    add_user(user.userid, user.password, user.firstname, user.lastname, user.email)
    return {"message": "User added"}

@app.get("/users/get/{user_id}")
def read_user(user_id: str):
    user = get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.delete("/users/remove/{user_id}")
def remove_user_route(user_id: str):
    remove_user(user_id)
    return {"message": "User removed"}

@app.put("/users/update_password/{user_id}/{password}")
def update_user_password_route(user_id: str, password: str):
    update_user_password(user_id, password)
    return {"message": "Password updated"}

@app.put("/users/update_email/{user_id}/{email}")
def update_user_email_route(user_id: str, email: str):
    update_user_email(user_id, email)
    return {"message": "Email updated"}

@app.put("/users/update_firstname/{user_id}/{firstname}")
def update_user_firstname_route(user_id: str, firstname: str):
    update_user_firstname(user_id, firstname)
    return {"message": "First name updated"}

@app.put("/users/update_lastname/{user_id}/{lastname}")
def update_user_lastname_route(user_id: str, lastname: str):
    update_user_lastname(user_id, lastname)
    return {"message": "Last name updated"}

@app.get("/users/get_all")
def read_all_users():
    users = get_all_users()
    return users

''' ----------- USER HEALTH ROUTES ----------- '''

@app.post("/userhealth/add_userhealth")
async def add_userhealth_route(userhealth: UserHealth):
    add_userhealth(userhealth.userid, userhealth.gender, userhealth.height, userhealth.weight, userhealth.age, userhealth.activity_level)
    return {"message": "User health added"}

@app.get("/userhealth/get/{user_id}")
def read_userhealth(user_id: str):
    userhealth = get_userhealth(user_id)
    if not userhealth:
        raise HTTPException(status_code=404, detail="User health not found")
    return userhealth

@app.delete("/userhealth/remove/{user_id}")
def remove_userhealth_route(user_id: str):
    remove_userhealth(user_id)
    return {"message": "User health removed"}

@app.put("/userhealth/update_gender/{user_id}/{gender}")
def update_userhealthgender_route(user_id: str, gender: str):
    update_userhealth_gender(user_id, gender)
    return {"message": "Gender updated"}

@app.put("/userhealth/update_height/{user_id}/{height}")
def update_userhealth_height_route(user_id: str, height: int):
    update_userhealth_height(user_id, height)
    return {"message": "Height updated"}

@app.put("/userhealth/update_weight/{user_id}/{weight}")
def update_userhealth_weight_route(user_id: str, weight: int):
    update_userhealth_weight(user_id, weight)
    return {"message": "Weight updated"}

@app.put("/userhealth/update_age/{user_id}/{age}")
def update_userhealth_age_route(user_id: str, age: int):
    update_userhealth_age(user_id, age)
    return {"message": "Age updated"}

@app.put("/userhealth/update_activity_level/{user_id}/{activity_level}")
def update_userhealth_activity_level_route(user_id: str, activity_level: str):
    update_userhealth_activity_level(user_id, activity_level)
    return {"message": "Activity level updated"}


''' -------------- INVENTORY ROUTES --------------- '''

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

@app.delete("/inventory/remove/{item_name}/{user_id}")
def remove_item_route(item_name: str, user_id: str):
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

@app.get("/inventory/get_json/{user_id}")
def read_inventory_products_and_quantities(user_id: int):
    inventory = get_inventory(user_id)
    if not inventory:
        raise HTTPException(status_code=404, detail="Inventory not found")
    products_and_quantities = {}
    for product, quantity in inventory:
        products_and_quantities[product] = quantity
    return products_and_quantities

@app.get("/inventory/get_recipes/{user_id}")
def get_all_recipes(user_id: int):
    all_products = get_all_products(user_id)
    if not all_products:
        raise HTTPException(status_code=404, detail="Inventory not found")
    product_list = []
    for product in all_products:
        product_list.append(product[0])

    return get_recipes(product_list)
    
