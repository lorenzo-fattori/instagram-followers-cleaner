import re

"""
This module processes text exported from Instagram account data.
It extracts usernames from raw followers/following blocks and finds
accounts you follow that do not follow you back.
"""

_USERNAME_RE = re.compile(r"^[a-zA-Z0-9._]{1,30}$")


def take_username(line: str) -> bool:
    """Return True if the line looks like a valid Instagram username."""
    candidate = line.strip()
    if not candidate:
        return False
    if candidate.startswith(("http://", "https://", "www.")):
        return False
    return _USERNAME_RE.fullmatch(candidate) is not None


def clean_input(text: str) -> list[str]:
    """Extract, normalize, and de-duplicate usernames preserving order."""
    usernames: list[str] = []
    seen: set[str] = set()

    for raw_line in text.splitlines():
        if not take_username(raw_line):
            continue

        username = raw_line.strip().lower()
        if username in seen:
            continue

        usernames.append(username)
        seen.add(username)

    return usernames


def not_following_back(followers: list[str], following: list[str]) -> list[str]:
    """Return a sorted list of users you follow who do not follow you back."""
    followers_set = set(followers)
    return sorted({user for user in following if user not in followers_set})
