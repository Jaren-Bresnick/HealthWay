from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import sys
sys.path.append('..')
from database.request_userhealth_db import add_userhealth, get_userhealth, remove_userhealth, update_userhealth_gender, update_userhealth_height, update_userhealth_weight, update_userhealth_age, update_userhealth_activity_level

class UserHealth(BaseModel):
    userid: str
    gender: str
    height: int
    weight: int
    age: int
    activity_level: str

app = FastAPI()

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



