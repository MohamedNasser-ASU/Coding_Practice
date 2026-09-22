def main():
    word = input("camelCase: ")
    print("snake_case: " , end = "")
    snake(word)
    print()
def snake(word):

    for c in word:
        if c.islower():
            print(c,end="")
        elif c.isupper():
            print("_" + c.lower() , end = "")

main()
