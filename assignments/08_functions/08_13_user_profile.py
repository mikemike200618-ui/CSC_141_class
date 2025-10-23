print("start with a copy of user_profile.py from 8_13.") 
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()
    for key, value in user_info.items():
        profile[key] = value
    return profile 
user_profile = build_profile('albert', 'einstein',location='princeton',field='physics') 
print(user_profile) 
# This function builds a user profile dictionary using required first and last name parameters,
# along with arbitrary keyword arguments for additional user information.
# It demonstrates how to use **kwargs to accept an arbitrary number of keyword arguments in Python. 
