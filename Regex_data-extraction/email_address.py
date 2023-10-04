import re

raw_data = input("Enter API data: ")

"""
For test cases, feel free to use this sample:
raw_data = "In today's digital age, communication has never been easier. Email has become a ubiquitous tool for professional and personal correspondence. For business inquiries, please reach out to info@example.com or contact our sales team at sales@companyxyz.com. Stay connected with us via support@helpdesk.com for any assistance."
"""

# Define a regular expression pattern to match email addresses
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

# Use re.findall to find all email addresses in the input text
matches = re.findall(pattern, raw_data)

# Print the extracted email addresses
if matches:
    print("Email addresses found:")
    for match in matches:
        print(match)
else:
    print("No email addresses found in the input.")
