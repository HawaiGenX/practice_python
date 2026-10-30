#DICTIONARIES
miami = {
    "name": "Miami",
    "state": "Florida",
    "population": 449514,
    "nickname": "Magic City",
}

new_york = {
    "name": "New York",
    "state": "New York",
    "population": 8258035,
    "nickname": "The Big Apple",
}

chicago = {
    "name": "Chicago",
    "state": "Illinois",
    "population": 2664452,
    "nickname": "The Windy City",
}

los_angeles = {
    "name": "Los Angeles",
    "state": "California",
    "population": 3820914,
    "nickname": "City of Angels",
}

houston = {
    "name": "Houston",
    "state": "Texas",
    "population": 2314157,
    "nickname": "Space City",
}

#LISTS OF DICTIONARIES
cities =[miami, new_york, chicago, los_angeles, houston]

for city in cities:
    print(f"\n{city}")