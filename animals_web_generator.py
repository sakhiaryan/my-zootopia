import json

def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

def print_animals_info(animals_data):
    """Prints Name, Diet, first Location and Type for each animal."""
    for animal in animals_data:
        name = animal.get("name")
        characteristics = animal.get("characteristics", {})
        diet = characteristics.get("diet")
        type_ = characteristics.get("type")
        locations = animal.get("locations", [])
        location_first = locations[0] if locations else None

        if name:
            print(f"Name: {name}")
        if diet:
            print(f"Diet: {diet}")
        if location_first:
            print(f"Location: {location_first}")
        if type_:
            print(f"Type: {type_}")
        print()  # empty line between animals


if __name__ == "__main__":
    animals_data = load_data("animals_data.json")
    print_animals_info(animals_data)