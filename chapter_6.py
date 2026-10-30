person_details = {
    "first_name": "Malik",
    "last_name": "Abdul",
    "age": 35,
    "phone_number": 435699478,
    "home_address": "55 Jonston Avenue",
    "home_city": "Johannesburg",  
}
print("\n")
# Use get() to avoid a KeyError when a key doesn't exist
name = person_details.get("first_name", "name does not exixt")
print(name)

print("\n")

for keys, values in person_details.items():
    print(f"{keys}: {values}")

print("\n")
