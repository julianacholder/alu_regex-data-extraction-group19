import re

raw_data = input("Enter API data: ")

""" 
for test cases, feel free to use this sample:
    raw_data = ABC123, PPP345, FTG345 lorem ipsum, lorem ipsum, raw data.
"""

pattern = r'([A-Z]{3}\d{3})'
matches = re.findall(pattern, raw_data)

for product_code in matches:
    print(product_code)