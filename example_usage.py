from instagram_cleaner import clean_input, not_following_back

# Example usage of the instagram_cleaner functions with sample data.
# In a real scenario, you would replace the raw strings with the actual text blocks 
# exported from Instagram's "Your Account Data" section for followers and following.
followers_raw = '''
some_follower1
some_follower2
some_follower3
'''
following_raw = '''
some_follower1
some_follower2
some_follower3
some_follower4
some_follower5
'''

# Process the raw input to extract valid usernames.
followers = clean_input(followers_raw)
following = clean_input(following_raw)

# Identify which users you follow that do not follow you back.
not_mutual = not_following_back(followers, following)

# Print the results.
print(f"Users not following back: {len(not_mutual)}")
for user in not_mutual:
    print(user)
    
# Output:
# Users not following back: 2
# some_follower4
# some_follower5
