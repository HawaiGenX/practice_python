aliens = []

for cities_number in range(30):
    alien_0 = {"color": "green", "points": 5, "x_position": 0, "y_position": 25, "speed": "medium","health": 100}
    aliens.append(alien_0)
for alien in aliens[:10]:
    print(f"\n{alien}")
print(".........")


