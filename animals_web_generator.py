import json
from pathlib import Path

DATA_FILE = Path("animals_data.json")
TEMPLATE_FILE = Path("animals_template.html")
OUTPUT_FILE = Path("animals.html")


def load_data(file_path):
    """Loads JSON data from a file."""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def html_escape(text):
    """Escape text for HTML (keep our tags intact by only escaping values)."""
    return (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&#39;")
    )


def build_animals_html(animals):
    """
    Build <li class="cards__item">…</li> blocks.
    Only include fields if present:
      - Name
      - Diet   (characteristics.diet)
      - Location (first of locations)
      - Type   (characteristics.type)
    """
    items = []

    for a in animals:
        lines = []

        name = a.get("name")
        if name:
            lines.append(f"Name: {html_escape(name)}<br/>")

        characteristics = a.get("characteristics", {}) or {}
        diet = characteristics.get("diet")
        if diet:
            lines.append(f"Diet: {html_escape(diet)}<br/>")

        locations = a.get("locations") or []
        if isinstance(locations, list) and locations:
            lines.append(f"Location: {html_escape(locations[0])}<br/>")

        type_ = characteristics.get("type")
        if type_:
            lines.append(f"Type: {html_escape(type_)}<br/>")

        if lines:
            items.append(f'<li class="cards__item">\n  ' + "\n  ".join(lines) + "\n</li>")

    return "\n".join(items)


def main():
    # 1) Load data
    animals = load_data(DATA_FILE)

    # 2) Build HTML list items
    html_cards = build_animals_html(animals)

    # 3) Read template
    template = TEMPLATE_FILE.read_text(encoding="utf-8")

    # 4) Replace placeholder
    html_out = template.replace("__REPLACE_ANIMALS_INFO__", html_cards)

    # 5) Write final HTML
    OUTPUT_FILE.write_text(html_out, encoding="utf-8")
    print(f"✅ Generated {OUTPUT_FILE}. Open it in your browser to preview.")


if __name__ == "__main__":
    main()