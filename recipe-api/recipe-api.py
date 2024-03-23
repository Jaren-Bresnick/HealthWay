import requests

def get_nutrition_and_link(recipe_id: str, ingredients: list[str]):
    url = "https://d1.supercook.com/dyn/details"

    payload = 'rid=' + recipe_id + '&lang=en&ingredients=' + '%2C'.join(ingredients)

    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json, text/plain, */*',
    'Sec-Fetch-Site': 'same-site',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, utf-8',
    'Sec-Fetch-Mode': 'cors',
    'Host': 'd1.supercook.com',
    'Origin': 'https://www.supercook.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15',
    'Referer': 'https://www.supercook.com/',
    'Content-Length': '153',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if not response.ok:
        print(f'Error sending nutrition request for id {recipe_id}:', response.status_code)
        return None, None

    recipe_data = response.json()
    nutrition_info = recipe_data['nutrition']
    if len(nutrition_info) == 0:
        print(f'No nutrition information found for id {recipe_id}')
        return None, None
    
    parsed_nutrition = {}
    for item in nutrition_info:
        name = item['name']
        value = item.get('value', None) 
        parsed_nutrition[name] = value

    nutrition = {
        "calories": parsed_nutrition.get("calories", None),
        "fat": parsed_nutrition.get("fat", None),
        "carbs": parsed_nutrition.get("carbs", None),
        "protein": parsed_nutrition.get("protein", None),
    }
    
    return nutrition, recipe_data['recipe']['hash']

def get_recipes(ingredients: list[str]):
    """
    Get recipes from SuperCook API based on ingredients

    :param ingredients: list of ingredients
    :return: list of recipe objects
    """

    url = "https://d1.supercook.com/dyn/results"

    for i in range(len(ingredients)):
        ingredients[i] = ingredients[i].lower()

    payload = 'needsimage=1&app=1&kitchen=' + '%2C'.join(ingredients) + '&focus=&exclude=&kw=&catname=&start=0&fave=false&lang=en&cv=2'
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Accept': 'application/json, text/plain, */*',
      'Sec-Fetch-Site': 'same-site',
      'Accept-Language': 'en-US,en;q=0.9',
      'Accept-Encoding': 'gzip, deflate, utf-8',
      'Sec-Fetch-Mode': 'cors',
      'Host': 'd1.supercook.com',
      'Origin': 'https://www.supercook.com',
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15',
      'Referer': 'https://www.supercook.com/',
      'content-length': '184',
      'Connection': 'keep-alive',
      'Sec-Fetch-Dest': 'empty'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if not response.ok:
        print('Error sending matching recipe request:', response.status_code)
        return
    
    json_response = response.json()
    recipe_raw_data = json_response['results']

    recipies = []

    for recipe in recipe_raw_data:
        
        if len(recipies) >= 10:
            return recipies
        
        nutrition, link = get_nutrition_and_link(recipe['id'], ingredients)

        recipe_to_add = {
            'id': recipe['id'],
            'title': recipe['title'],
            'img_url': recipe['img'],
            'domain': recipe['domain'],
            'nutrition': nutrition,
            'link': link
        }
        
        recipies.append(recipe_to_add)
    
    return recipies

# Example usage
print(get_recipes(['garlic', 'flour', 'tomato', 'celery']))
