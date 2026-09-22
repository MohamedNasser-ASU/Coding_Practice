fruits = {
    "apple" : "130",
    "avocado" : "50",
    "sweet cherries" : "100",
    "kiwifruit" : "90",
    "pear" : "100",
}

word = input("Item: ").lower().strip()
if word in fruits:
    print("Calories: ", end = "")
    print(fruits[word])
