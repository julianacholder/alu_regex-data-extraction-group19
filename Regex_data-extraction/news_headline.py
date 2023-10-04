import re

# Sample raw API response containing news data
raw_text = "This is a sample headline - Subheader: This is a sample subheader"

# Define the regular expression pattern to match news headlines
news_headline_regex = r"(.+?) - (.+?)"

# Use re.search to find the first match in the raw text
match = re.search(news_headline_regex, raw_text)

# Check if a match was found
if match:
    # Extract the news headline from the first capturing group (group 1)
    news_headline = match.group(1).strip()
    print("News Headline:", news_headline)
else:
    print("No news headline found in the raw text.")

