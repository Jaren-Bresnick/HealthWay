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
image_dir = Path("images/test")

# Validate that the directory exists
if not image_dir.exists() or not image_dir.is_dir():
    raise FileNotFoundError(f"Could not find directory: {image_dir}")

# List to store combined food items from all images
all_food_items = []

# List of image formats to process
image_formats = ["*.jpeg", "*.jpg", "*.png"]

# Loop through each image format
for img_format in image_formats:
    # Loop through each image in the images directory for the current format
    for image_path in image_dir.glob(img_format):
        # Determine the correct MIME type based on the file extension
        if image_path.suffix.lower() == ".png":
            mime_type = "image/png"
        else:
            mime_type = "image/jpeg"
        
        # Prepare the image part for the API request
        image_parts = [
            {
                "mime_type": mime_type,
                "data": image_path.read_bytes()
            },
        ]

        prompt_parts = [
            image_parts[0],
            "\nGiven the image of the fridge, please generate a json file of 'food_items' that are present in the fridge and the quantity of each. Only put foods and items in the list that you are 70 percent sure of."
        ]

        # Generate content for each image
        response = model.generate_content(prompt_parts)
        response_text = response.text  # Assuming 'text' attribute holds the response; adjust as needed

        #Remove ```json from the response
        response_text = response.text.replace('```json', '')

        #Remove ``` from the response
        response_text = response_text.replace('```', '')

        print(response_text)

        # Assuming response_text is directly parseable JSON; adjust if your actual response format differs
        try:
            food_data = json.loads(response_text)
            all_food_items.extend(food_data["food_items"])
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from response for image {image_path}: {e}")


# Combine all food items into one JSON object
combined_food_data = {"food_items": all_food_items}

# Print or save the combined JSON
#print(json.dumps(combined_food_data, indent=2))

# After processing all images and combining the data
# Assuming 'name' key exists for each food item in your JSON structure

# Extract just the names of the food items from the combined data
food_names = [item["name"] for item in combined_food_data["food_items"]]

# Print the list of food names
print("Food items found in all images:", ", ".join(food_names))

