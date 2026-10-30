favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
    "amara": "javascript",
    "diego": "java",
    "priya": "c++",
    "kenji": "go",
    "fatima": "swift",
    "lucas": "kotlin",
}
print("\n")
people = ["jen", "marcus", "olivia"]
for person in people:
    if person in favorite_languages:
        print(f"\n{person.title()}, Thank you for taking the poll")
    else:
        print(f"\n{person.title()}, please take our poll")
print("\n")