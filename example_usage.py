from instagram_cleaner import clean_input, not_following_back

followers_raw = '''
user1
user2
'''
following_raw = '''
user1
user2
user3
user4
'''

followers = clean_input(followers_raw)
following = clean_input(following_raw)

not_mutual = not_following_back(followers, following)

print(f"Users not following back: {len(not_mutual)}")
for user in not_mutual:
    print(user)
