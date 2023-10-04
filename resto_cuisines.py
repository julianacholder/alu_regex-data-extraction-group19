import re

# Prompting the user to enter raw data.
raw_data = input("Enter API data: ")

""" 
for test cases, feel free to use this sample:
    raw_data = Mariot Hotel - Italian , Serena Hotels - Chinese, lorem ipsum lorem ipsum
"""

pattern = r'([A-Za-z\s]+) - ([A-Za-z\s]+)'
matches = re.findall(pattern, raw_data)

for match in matches:
    restaurant_name, cuisine_type = match
    print(f"{restaurant_name.strip()} - {cuisine_type.strip()}")