from pathlib import Path
import google.generativeai as genai
import json

def configure_genai():
    genai.configure(api_key="AIzaSyDiyZENflOTXzGKCmSaDZsxZ1ts8BoJnqo")

def identify_pills_in_image(data, mimetype):
  
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
      "\nGiven the prescription bottle label, please generate a json file of 'prescription_items'. Identify values Name, dose size, pill count, refill date, expiry date, description of medication, and pills used per day as an integer. Only put pills in the list that you are 70 percent sure of."
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
      prescription_data = json.loads(response_text)
      pill_info = [item["name"] for item in prescription_data['prescription_items']]
      return prescription_data
  except json.JSONDecodeError as e:
      print(f"Error decoding JSON from response for image: {e}")
      return []

def main(image_path):
    configure_genai()
    # Call the function to process the single image file
    pill_info = identify_pills_in_image(image_path)
    return pill_info

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Please provide an image path.")
