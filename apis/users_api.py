from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import sys
sys.path.append('..')
from database.request_users_db import add_user, get_user, remove_user, update_user_email, update_user_firstname, update_user_lastname, update_user_password, get_all_users, test, addnewtable

class User(BaseModel):
    userid: str
    password: str
    firstname: str
    lastname: str
    email: str

app = FastAPI()


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
