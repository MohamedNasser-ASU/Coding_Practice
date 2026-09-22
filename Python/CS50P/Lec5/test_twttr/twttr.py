def main():
    word = input("Input: ").strip()
    print("Output: ", end="")
    print(shorten(word))

def shorten(word):
    string = ""
    for c in word:
        if c not in ['a', 'e', 'i', 'o', 'u']:
            #print(c, end="")
            string = string + c
    return string

if __name__ == "__main__":
    main()
