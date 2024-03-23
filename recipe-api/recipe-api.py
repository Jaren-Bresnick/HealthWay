import requests

def get_recipes(ingredients: list[str]):
    """
    Get recipes from SuperCook API based on ingredients

    :param ingredients: list of ingredients
    :return: list of recipe objects
    """

    url = "https://d1.supercook.com/dyn/results"

    for ingredient in ingredients:
        ingredient = ingredient.lower()

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
      'Content-Length': '184',
      'Connection': 'keep-alive',
      'Sec-Fetch-Dest': 'empty'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if not response.ok:
        print('Error sending request:', response.status_code)
        return
    
    json_response = response.json()
    recipies = json_response['results']
    return recipies

# Example usage
get_recipes(['Egg', 'cinnamon', 'soy sauce', 'butter', 'apple', 'sugar', 'banana', 'brown sugar', 'biscuit dough', 'sldkfjsldkjf'])