from pathlib import Path
import google.generativeai as genai
import json

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

# Directory containing images
image_dir = Path("images")

# Validate that the directory exists
if not image_dir.exists() or not image_dir.is_dir():
    raise FileNotFoundError(f"Could not find directory: {image_dir}")

# List to store combined food items from all images
all_food_items = []

# Loop through each image in the images directory
for image_path in image_dir.glob("*.jpeg"):  # Assuming JPEG format; adjust if necessary
    image_parts = [
        {
            "mime_type": "image/jpeg",
            "data": image_path.read_bytes()
        },
    ]

    prompt_parts = [
        image_parts[0],
        "\nGiven the image of the fridge or food, please generate a json file of food items that are present in the fridge and the quantity of each."
    ]

    # Generate content for each image
    response = model.generate_content(prompt_parts)
    response_text = response.text  # Assuming 'text' attribute holds the response; adjust as needed
    print(response_text)

    #Remove ```json from the response
    response_text = response.text.replace('```json', '')

    #Remove ``` from the response
    response_text = response_text.replace('```', '')

    # Remove any leading/trailing formatting if necessary
    # Assuming response_text is directly parseable JSON; adjust if your actual response format differs
    try:
        food_data = json.loads(response_text)
        all_food_items.extend(food_data["food_items"])
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from response for image {image_path}: {e}")

# Combine all food items into one JSON object
combined_food_data = {"food_items": all_food_items}

# Print or save the combined JSON
# print(json.dumps(combined_food_data, indent=2))

# After processing all images and combining the data
# Assuming 'name' key exists for each food item in your JSON structure

# Extract just the names of the food items from the combined data
food_names = [item["name"] for item in combined_food_data["food_items"]]

# Print the list of food names
print("Food items found in all images:", ", ".join(food_names))

