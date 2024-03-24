from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sys
sys.path.append('../food_recognition')
import food_recognition
import receipt_recognition
import stocking_recognition
import inventory_api

app = FastAPI()

class Item(BaseModel):
    product: str
    quantity: int
    userid: str

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
    elif type_of_image == "stocking":
        json_file = stocking_recognition.main()
    else:
        raise HTTPException(status_code=400, detail="Invalid image type. Please enter 'receipt', 'pantry', or 'stocking'.")

    # Assuming json_file is a dict with the required structure
    if not json_file or "food_items" not in json_file or not json_file["food_items"]:
        raise HTTPException(status_code=400, detail="No food items found or incorrect JSON structure.")

    # Convert json file output to an 'item' object and take quantity from json file
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
