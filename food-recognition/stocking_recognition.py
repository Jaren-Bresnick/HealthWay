import json
import food_recognition
from motion_recognition import detect_and_track_object

def process_images_and_detect_motion(image_paths):
    # Process the first image to identify food items.
    # Assuming 'identify_food_in_image' returns a list of dictionaries with 'name' and 'quantity'
    food_items = food_recognition.main(image_paths[0])

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

# Example usage:
image_paths = ["images/bottle_candy_1.jpg", "images/bottle_candy_2.jpg"]
json_output = process_images_and_detect_motion(image_paths)
print(json_output)
