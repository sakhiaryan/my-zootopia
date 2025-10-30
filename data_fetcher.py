# data_fetcher.py
import os
import requests
from dotenv import load_dotenv
load_dotenv()

BASE_URL = "https://api.api-ninjas.com/v1/animals"
API_KEY = os.getenv("ANIMALS_API_KEY")

def fetch_data(animal_name: str):
    """
    Fetch animals for 'animal_name' from API Ninjas.
    Returns list[dict] or [] on not found/error.
    """
    if not animal_name or not animal_name.strip():
        return []
    if not API_KEY:
        print("Warning: ANIMALS_API_KEY is not set.")
        return []

    url = f"{BASE_URL}?name={animal_name.strip()}"
    headers = {"X-Api-Key": API_KEY}
    try:
        resp = requests.get(url, headers=headers, timeout=15)
        print("Status Code:", resp.status_code)
        if resp.status_code == 200:
            data = resp.json()
            return data if isinstance(data, list) else []
        else:
            print("Error body:", resp.text)
            return []
    except requests.RequestException as e:
        print("Network/API error:", e)
        return []