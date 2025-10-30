import json
import requests
import os
from pathlib import Path

TEMPLATE_FILE = Path("animals_template.html")
OUTPUT_FILE = Path("animals.html")


API_KEY = os.getenv("ANIMALS_API_KEY")
BASE_URL = "https://api.api-ninjas.com/v1/animals"


def fetch_animals(animal_name):
    """Fetch animal data from the API."""
    url = f"{BASE_URL}?name={animal_name}"
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(url, headers=headers)
    print("Status Code:", response.status_code)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error:", response.text)
        return []


def build_animals_html(animals, animal_name):
    """Build HTML for all animals or show error if empty."""
    if not animals:
        return f'<h2>The animal "{animal_name}" doesn\'t exist.</h2>'

    items = []
    for a in animals:
        name = a.get("name", "Unknown")
        characteristics = a.get("characteristics", {})
        diet = characteristics.get("diet", "Unknown")
        location = a.get("locations", [])
        type_ = characteristics.get("type", "Unknown")

        locations = ", ".join(location) if isinstance(location, list) else location

        item_html = f"""
        <li class="cards__item">
            <div class="card__title">{name}</div>
            <div class="card__text">
                <ul class="card__list">
                    <li><strong>Diet:</strong> {diet}</li>
                    <li><strong>Location:</strong> {locations}</li>
                    <li><strong>Type:</strong> {type_}</li>
                </ul>
            </div>
        </li>
        """
        items.append(item_html)

    return "\n".join(items)


def main():
    animal_name = input("Enter a name of an animal: ").strip()
    animals = fetch_animals(animal_name)

    html_animals = build_animals_html(animals, animal_name)

    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        template = f.read()

    html_out = template.replace("__REPLACE_ANIMALS_INFO__", html_animals)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html_out)

    print(f"✅ Website was successfully generated to the file {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
