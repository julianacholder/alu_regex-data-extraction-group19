import re

raw_data = input("Enter API data: ")

""" 
for test cases, feel free to use this sample:
    raw_data = "Check out @username123's profile and follow @chrisos10"
"""

pattern = r'@([A-Za-z0-9]+)'
matches = re.findall(pattern, raw_data)

for username in matches:
    print(f"@{username}")