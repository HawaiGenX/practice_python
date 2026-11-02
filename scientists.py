users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },

    }
print("\n")
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    name = full_name.replace("_", " ")
    location = user_info["location"]
    print(f"\tUser full name: {name}")
    print(f"\tUser location: {location}")
print("\n")
