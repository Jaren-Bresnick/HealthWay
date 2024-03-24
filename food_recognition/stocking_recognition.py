import json
import food_recognition
from motion_recognition import detect_and_track_object
from pathlib import Path
import mimetypes

def process_images_and_detect_motion(image_paths):
    # Process the first image to identify food items.
    # Assuming 'identify_food_in_image' returns a list of dictionaries with 'name' and 'quantity'
    data = Path(image_paths[0]).read_bytes()
    mimetype, _ = mimetypes.guess_type(image_paths[0])
    food_items = food_recognition.identify_food_in_image(data, mimetype)

    # Detect and track the motion of objects in the images.
    # Assuming 'detect_and_track_object' returns a string indicating the direction of movement
    direction = detect_and_track_object(image_paths)


    # Combine the food items with the direction of motion
    items_with_motion = {
        "food_items": food_items["food_items"][0]["name"],
        "quantity": food_items['food_items'][0]['quantity'],
        "motion": direction
    }

    # Convert the result to JSON
    json_result = json.dumps(items_with_motion)
    return json_result

if __name__ == "__main__":
    print(process_images_and_detect_motion(["images/frame_1.jpg", "images/frame_2.jpg"]))