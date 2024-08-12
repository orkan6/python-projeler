item = input("Item: ").lower()
calcount = [
    {"fruit": "apple", "callories": "130"},
    {"fruit": "avocado", "callories": "50"},
    {"fruit": "banana", "callories": "110"},
    {"fruit": "cantaloupe", "callories": "50"},
    {"fruit": "grapefruit", "callories": "60"},
    {"fruit": "grapes", "callories": "90"},
    {"fruit": "honeydew melon", "callories": "50"},
    {"fruit": "kiwifruit", "callories": "90"},
    {"fruit": "pear", "callories": "100"},
    {"fruit": "sweet cherries", "callories": "100"}
]

for meyve in calcount:
    if item in meyve["fruit"]:
        print("Calories:", meyve["callories"])
