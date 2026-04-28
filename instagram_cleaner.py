import re
'''
This script is designed to process the text block exported from Instagram's "Your Account Data" section, 
specifically the list of followers and following. 
It extracts only the usernames and identifies which users you follow that do not follow you back.    
'''

# this function checks if a line from the input text is a valid username, filtering out links, dates, and empty lines.
def take_username(line):
    """Return True if the line is a valid username (no link, no data)."""
    if line.startswith("http"):
        return False
    # exludes dates like "dic 04, 2025 3:19 pm"
    if re.search(r"\d{4}", line):
        return False
    if line.strip() == "":
        return False
    return True

# this function takes the raw text input, splits it into lines, and applies the take_username filter to extract only valid usernames.
def clean_input(text):
    """Extracts only usernames from an exported Instagram text block"""
    lines = text.splitlines()
    return [r.strip() for r in lines if take_username(r)]

# this function compares the list of followers and following to identify which users you follow that do not follow you back.
def not_following_back(followers, following):
    """Returns the list of users you follow but don't follow you back."""
    return {u for u in following if u not in followers}
