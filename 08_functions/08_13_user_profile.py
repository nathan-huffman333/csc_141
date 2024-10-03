# This code receives my first and last name and multiple keyword arguments of information about me to create a profile.

import os
os.system('cls')

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('nathan', 'huffman',
                            location='reading',
                            field='computer science',
                            hobby='video games')
print(user_profile)