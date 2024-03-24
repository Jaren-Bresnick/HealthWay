import json
from motion_recognition import detect_and_track_object
from pathlib import Path
import mimetypes
import google.generativeai as genai


def process_images_and_detect_motion(image_paths):
    # Process the first image to identify food items.
    # Assuming 'identify_food_in_image' returns a list of dictionaries with 'name' and 'quantity'
    data = Path(image_paths[0]).read_bytes()
    mimetype, _ = mimetypes.guess_type(image_paths[0])
    # food_items = identify_food_in_image(data, mimetype)

    genai.configure(api_key="AIzaSyDiyZENflOTXzGKCmSaDZsxZ1ts8BoJnqo")
    # Set up the model configuration
    generation_config = {
        "temperature": 0.4,
        "top_p": 1,
        "top_k": 32,
        "max_output_tokens": 4096,
    }

    safety_settings = [
        {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
    ]

    model = genai.GenerativeModel(model_name="gemini-1.0-pro-vision-latest",
                                    generation_config=generation_config,
                                    safety_settings=safety_settings)

    # Prepare the image part for the API request
    image_parts = [
        {
            "mime_type": mimetype,
            "data": data
        },
    ]

    prompt_parts = [
        image_parts[0],
        "\nGiven the image, please generate a json file of 'food_items' that are present and the quantity of each. Only put foods and items in the list that you are 70 percent sure of."
    ]

    # Generate content for the image
    response = model.generate_content(prompt_parts)
    response_text = response.text

    #Remove ```json from the response
    response_text = response.text.replace('```json', '')

    #Remove ``` from the response
    response_text = response_text.replace('```', '')

    # Assuming response_text is directly parseable JSON; adjust if your actual response format differs
    try:
        food_data = json.loads(response_text)
        food_items = [item["name"] for item in food_data["food_items"]]
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from response for image: {e}")
        return []

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