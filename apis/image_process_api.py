from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pathlib import Path
import sys
import os
sys.path.append(os.path.abspath('../food_recognition'))
sys.path.append(os.path.abspath('../pills_recognition'))
import food_recognition
import receipt_recognition
import motion_recognition
import stocking_recognition
import pills_recognition

app = FastAPI()

class Item(BaseModel):
    product: str
    quantity: int
    userid: str

class Pill(BaseModel):
    product: str
    dosage: str
    quantity: int
    refill_date: str
    expiration_date: str

class ImageData(BaseModel):
    type_of_image: str
    image_path: str = None

@app.post("/process_image/")
def process_image(data: ImageData):
    type_of_image = data.type_of_image
    image_path = data.image_path
    json_file = ""

    if type_of_image == "receipt":
        json_file = receipt_recognition.identify_food_in_image(image_path)
    elif type_of_image == "pantry":
        json_file = food_recognition.identify_food_in_image(image_path)
    elif type_of_image == "pills":
        json_file = pills_recognition.identify_pills_in_image(image_path)
    elif type_of_image == "stocking":
        json_file = stocking_recognition.main()
    else:
        raise HTTPException(status_code=400, detail="Invalid image type. Please enter 'receipt', 'pantry', or 'stocking'.")

    # Assuming json_file is a dict with the required structure
    if not json_file or "food_items" not in json_file or not json_file["food_items"]:
        raise HTTPException(status_code=400, detail="No food items found or incorrect JSON structure.")

    if type_of_image == "pills":
        pill = Pill(product=json_file["pills"][0]["name"],
                    dosage=json_file["pills"][0]["dosage"],
                    quantity=json_file["pills"][0]["quantity"],
                    refills=json_file["pills"][0]["refill_date"],
                    expiration_date=json_file["pills"][0]["expiration_date"])

        inventory_api.add_or_update_pill(pill)

    # Convert json file output to an 'item' object and take quantity from json file
    elif type_of_image in ["receipt", "pantry", "stocking"]:
        item = Item(product=json_file["food_items"][0]["name"],
                    quantity=json_file["food_items"][0]["quantity"],
                    userid="1")

    # If the image is a receipt or pantry, add/update the item to inventory
    # If the image is stocking, the action should be determined by the main function of stocking_recognition
    if type_of_image in ["receipt", "pantry"]:
        inventory_api.add_or_update_item(item)
    elif type_of_image == "stocking":
        if json_file["motion"] == "Out":
            inventory_api.remove_item_route(item)
        elif json_file["motion"] == "In":
            inventory_api.add_item_route(item)

    return {"message": "Processed successfully", "item": item}
