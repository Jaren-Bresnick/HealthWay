import re

json_string = '{"food_items": [{"name": "orange", "quantity": 2}, {"name": "carrot", "quantity": 5}, {"name": "tomato", "quantity": 2}, {"name": "grapefruit", "quantity": 1}]}'

# Pattern to match the "name": "value" part of the string, capturing the value part
pattern = r'"name": "([^"]+)"'

# Using re.findall to find all matches of the pattern in the json_string
matches = re.findall(pattern, json_string)

# Joining the extracted names into a single string, separated by commas
items_string = ', '.join(matches)

print(items_string)