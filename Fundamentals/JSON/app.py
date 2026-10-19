import json
from pathlib import Path

person = '{"name": "Bob", "languages": ["English", "French"]}'

# JSON to dict

person_dict = json.loads(person)
print("\nJSON to Dict: ", person_dict)

print("\nLanguages: ", person_dict["languages"])


# read JSON file

script_dir = Path(__file__).parent
print("\nCurrent DIR: ", script_dir)
file_path = script_dir / "person.json"
print("File Path: ", file_path)


with open(file_path, "r") as f:
    data = json.load(f)

print(data)

# dict to JSON

json_from_dict = json.dumps(data)
print("\nDict to JSON: ", json_from_dict)

# Pretty Printing JSON string back
pretty = json.dumps(data, indent=4, sort_keys=True)
print("\nPretty Printing JSON string back: \n", pretty)
