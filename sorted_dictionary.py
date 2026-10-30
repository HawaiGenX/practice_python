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
#Sort the keys in an alphabetical order using method sorted()
for name in sorted(favorite_languages.keys()):
    print(f"\n{name.title()}, thank you for taking our poll")
print("\n") 