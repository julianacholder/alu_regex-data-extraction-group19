import re 

raw_data = input("Enter API data: ")


# The regular expression pattern to match the headlines
pattern = r"^([^:]+):\s*(.+)$"

#Find all matching headlines

matches = re.findall(pattern, raw_data)

# Extract newsheadline and subheader
newsHeadlines=[]
for match in matches:
        # Extract the headline and subheader from the match
        headline = match.group("headline")
        subheader = match.group("subheader")

        # Append the tuple (headline, subheader) to the headlines list
        newsHeadlines.append((headline, subheader))

    # Return the list of extracted headlines
    return newsHeadlines


if matches:
    print("News headlines found:")
    for match in matches:
        print(match)
else:
    print("No news headlines found in the input.")
