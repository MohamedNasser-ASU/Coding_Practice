def main():
    word = input("Input: ").strip()
    print("Output: ", end="")
    vow(word)
    print()

def vow(word):
    for c in word:
        if c.lower() not in ['a', 'e', 'i', 'o', 'u']:
            print(c, end="")
main()
