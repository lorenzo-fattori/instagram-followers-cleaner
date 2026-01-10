import re

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


def clean_input(text):
    """Extracts only usernames from an exported Instagram text block"""
    lines = text.splitlines()
    return [r.strip() for r in lines if take_username(r)]


def not_following_back(followers, following):
    """Returns the list of users you follow but don't follow you back."""
    return {u for u in following if u not in followers}
