def main():
    x = int(input("X = "))
    if isEven(x):
        print("Even")
    else:
        print("Odd")


def isEven(n):

    # normal way:
    # if n % 2 == 0:
    #     return True
    # else:
    #     return False

    # good way
    # return True if n % 2 == 0 else False

    # better way
    return ( n % 2 == 0)

main()
