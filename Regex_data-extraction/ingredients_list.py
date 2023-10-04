import re

raw_data = input("Enter API data: ")

# Pattern: "ingredient1, ingredient2, ingredient3"
pattern = r"^(?P<ingredients>.*?)(?:,\s*|$)"
matches = re.search(pattern, raw_data)
# Check if a match is found
if matches:
  print("Ingredients have been found")
  ingredients_str = matches.group("ingredients").strip()
# Remove leading/trailing whitespaces
  print(ingredients_str.split(", "))
  else:
     print("No ingredients found in input")
