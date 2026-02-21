import requests
from django.conf import settings

def get_recipe_from_groq(ingredients):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {settings.GROQ_API_KEY}",
        "Content-Type": "application/json",
    }

    prompt = f"Generate a unique recipe using the following ingredients: {','.join(ingredients)}. Include step-by-step instructions and a name for the dish. and one more important if ingredients was not related to food don't suggest instead replay not possible"
  
    payload = {
    "model": "llama-3.1-8b-instant",
    "messages": [
        {"role": "system", "content": "You are a helpful AI chef."},
        {"role": "user", "content": prompt}
    ],
    "temperature": 0.8
}

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print(data)
        return data["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code} - {response.text}"
