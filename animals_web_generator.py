# animals_web_generator.py
from pathlib import Path
import data_fetcher

TEMPLATE_FILE = Path("animals_template.html")
OUTPUT_FILE = Path("animals.html")

def build_animals_html(animals, animal_name: str) -> str:
    if not animals:
        return f"""
        <div style="text-align:center; margin-top:50px;">
            <h2>The animal "{animal_name}" doesn't exist 🐾</h2>
            <p>Please try another one, e.g. <strong>Fox</strong> or <strong>Monkey</strong>.</p>
        </div>
        """

    items = []
    for a in animals:
        name = a.get("name", "Unknown")
        characteristics = a.get("characteristics", {}) or {}
        diet = characteristics.get("diet", "Unknown")
        type_ = characteristics.get("type", "Unknown")
        locations = a.get("locations", [])
        locations_str = ", ".join(locations) if isinstance(locations, list) else str(locations)

        item_html = f"""
        <li class="cards__item">
            <div class="card__title">{name}</div>
            <div class="card__text">
                <ul class="card__list">
                    <li class="card__list-item"><span class="label">Diet:</span> {diet}</li>
                    <li class="card__list-item"><span class="label">Location:</span> {locations_str}</li>
                    <li class="card__list-item"><span class="label">Type:</span> {type_}</li>
                </ul>
            </div>
        </li>
        """
        items.append(item_html)

    return "\n".join(items)

def main():
    animal_name = input("Please enter an animal: ").strip()
    animals = data_fetcher.fetch_data(animal_name)

    html_animals = build_animals_html(animals, animal_name)

    template = TEMPLATE_FILE.read_text(encoding="utf-8")
    html_out = template.replace("__REPLACE_ANIMALS_INFO__", html_animals)
    OUTPUT_FILE.write_text(html_out, encoding="utf-8")

    print(f"✅ Website was successfully generated to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()