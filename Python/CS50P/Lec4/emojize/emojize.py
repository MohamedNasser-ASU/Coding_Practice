from emoji import emojize
def main():
    x = input("Input: ")
    print("Output: " + emojize(x, language='alias'))


main()
