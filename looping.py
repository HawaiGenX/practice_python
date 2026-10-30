person_details = {
    "first_name": "Malik",
    "last_name": "Abdul",
    "age": 35,
    "phone_number": 435699478,
    "home_address": "55 Jonston Avenue",
    "home_city": "Johannesburg",
}
# Looping through key-value
for key, value in person_details.items():
    print(f"\n{key.title()}: {value}")
print("\n")

# Looping through keys
for key in person_details.keys():
    print(f"{key.title()}")  
print("\n")

# OR

print("\n")
for key in person_details:
    print(f"{key.title()}")
print("\n")
