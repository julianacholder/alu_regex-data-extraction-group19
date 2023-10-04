import re

raw_data = input("Enter API data: ")

""" 
for test cases, feel free to use this sample:
    raw_data = "Events: Oct 12, 2023 - 02:30 PM, Nov 15, 2023 - 08:00 AM".
"""

pattern = r'(\w+ \d{1,2}, \d{4}) - (\d{2}:\d{2} [APap][Mm])'
matches = re.findall(pattern, raw_data)

for match in matches:
    event_date, event_time = match
    print(f"{event_date} - {event_time}")
