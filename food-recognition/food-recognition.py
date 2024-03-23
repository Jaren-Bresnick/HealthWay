"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

from pathlib import Path
import google.generativeai as genai
import json
import re

genai.configure(api_key="YOUR_API_KEY")

# Set up the model
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

# Validate that an image is present
if not (img := Path("tomatocarrot.jpg")).exists():
  raise FileNotFoundError(f"Could not find image: {img}")

image_parts = [
  {
    "mime_type": "image/jpeg",
    "data": Path("tomatocarrot.jpg").read_bytes()
  },
]

prompt_parts = [
  image_parts[0],
  "\nGiven the image of the fridge, please generate a json file of food items that are present in the fridge and the quantity of each."
]


response = model.generate_content(prompt_parts) 

# Print the response

print(response.text)

#Remove ```json from the response
response_text = response.text.replace('```json', '')

#Remove ``` from the response
response_text = response_text.replace('```', '')

#Convert response_text into a json object
response_json = json.loads(response_text)

# Pattern to match the "name": "value" part of the string, capturing the value part
pattern = r'"name": "([^"]+)"'

# Using re.findall to find all matches of the pattern in the json_string
matches = re.findall(pattern, response.text)

# Joining the extracted names into a single string, separated by commas
items_string = ', '.join(matches)

print(items_string)