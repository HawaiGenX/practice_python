aliens = []

for aliens_number in range(30):
    alien_0 = {
        "color": "green",
        "points": 5,
        "x_position": 0,
        "y_position": 25,
        "speed": "medium",
        "health": 100,
    }
    aliens.append(alien_0)
# CHANGE THE FIRST 3 ALIENS COLOR, SPEED, AND POINTS
for alien in aliens[:3]:
    if alien["color"]=="green":
        alien["color"] = "yellow"
        alien["speed"] = "fast"
        alien["points"] = 10
    elif alien["color"]=="yellow":
        alien["color"] = "red"
        alien["speed"] = "super fast"
        alien["points"] = 15
# PRINT ONLY 5 OUT 30 ALIENS
for alien in aliens[:5]:
    print(alien)
print(".......")



