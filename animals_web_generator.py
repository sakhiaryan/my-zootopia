import json
from pathlib import Path

# Define file paths
DATA_FILE = Path("animals_data.json")
TEMPLATE_FILE = Path("animals_template.html")
OUTPUT_FILE = Path("animals.html")


def load_data(file_path):
    """Loads JSON data from a file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def build_animals_text(animals):
    """Builds a text block with all animal information."""
    blocks = []

    for animal in animals:
        lines = []

        name = animal.get("name")
        if name:
            lines.append(f"Name: {name}")

        characteristics = animal.get("characteristics", {})
        diet = characteristics.get("diet")
        if diet:
            lines.append(f"Diet: {diet}")

        locations = animal.get("locations", [])
        if locations:
            lines.append(f"Location: {locations[0]}")

        type_ = characteristics.get("type")
        if type_:
            lines.append(f"Type: {type_}")

        if lines:
            blocks.append("\n".join(lines))

    # Separate animals with a blank line
    return "\n\n".join(blocks)


def html_escape(text):
    """Escapes HTML special characters and converts newlines to <br>."""
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return text.replace("\n", "<br>\n")


def main():
    # 1️⃣ Load JSON data
    animals = load_data(DATA_FILE)

    # 2️⃣ Build the text
    plain_text = build_animals_text(animals)

    # 3️⃣ Read HTML template
    with open(TEMPLATE_FILE, "r", encoding="utf-8") as file:
        template = file.read()

    # 4️⃣ Replace the placeholder with the generated text
    html_animals = html_escape(plain_text)
    html_out = template.replace("__REPLACE_ANIMALS_INFO__", html_animals)

    # 5️⃣ Write the new HTML file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        file.write(html_out)

    print(f"✅ File '{OUTPUT_FILE}' was successfully generated!")


if __name__ == "__main__":
    main()