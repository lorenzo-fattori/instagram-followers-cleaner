# instagram-follower-cleaner
A small Python utility to clean Instagram exported text and detect users who do not follow back.

This project was built as part of my learning journey while studying Python fundamentals, with a focus on clean code, text processing, and data cleaning.

This project is intentionally simple and focused on fundamentals.
It represents an early step in my learning path.

---

## Features
- Cleans raw Instagram export text
- Removes links, dates, and empty lines
- Normalizes usernames (lowercase, stripped)
- Detects users you follow who do not follow you back
- Efficient comparison using Python sets

---

## Example Usage

```python
from instagram_cleaner import clean_input, not_following_back

followers_text = """
user1
user2
"""

following_text = """
user1
user2
user3
"""

followers = clean_input(followers_text)
following = clean_input(following_text)

not_mutual = not_following_back(followers, following)

print("Users not following back:")
for user in not_mutual:
    print(user)
```
Output:
```yaml
Users not following back:
user3
```

---

## Project structure
```bash
instagram-followers-cleaner/
│
├── instagram_cleaner.py   # Core logic
├── example_usage.py       # Simple usage example
└── README.md              # Project documentation
```
