from instagram_cleaner import clean_input, not_following_back

followers_raw = '''
some_follower1
some_follower2
some_follower3
'''
following_raw = '''
some_follower1
some_follower4
some_follower5
'''

followers = clean_input(followers_raw)
following = clean_input(following_raw)

not_mutual = not_following_back(followers, following)

print(f"Users not following back: {len(not_mutual)}")
for user in not_mutual:
    print(user)
    
# Output:
# Users not following back: 2
# some_follower4
# some_follower5
