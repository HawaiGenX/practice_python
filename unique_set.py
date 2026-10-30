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
    "maria": "python",
    "omar": "java",
    "chloe": "javascript",
    "ravi": "c++",
    "nadia": "python",
    "tomas": "rust",
    "aisha": "java",
    "ben": "go",
    "lena": "javascript",
    "samuel": "python",
}
print("\n")
#How to print values without repeating using set() method
print("The following languages have been mentioned")
for languages in set(favorite_languages.values()):
    print(f"{languages}")
print("\n")
