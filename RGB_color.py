import re

raw_data = input("Enter API data: ")

""" 
for test cases, feel free to use this sample:
    raw_data = rgb(255, 255, 255) and rgb(0, 128, 64) colors, lorem ipsum lorem ipsum rgb(100, 344, 155)
"""

pattern = r'rgb\((\d+), (\d+), (\d+)\)'
matches = re.findall(pattern, raw_data)

for match in matches:
    r, g, b = match
    print(f"rgb({r}, {g}, {b})")