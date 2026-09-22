# x = float(input("X = "))
# y = float(input("Y = "))
# z = round(x + y)
# print(f"{z:,}") # X,YZQ

def main():
    x = int(input("X = "))
    print(f"X squared = {square(x)}")

def square(num = 0):
    # return num * num
    return pow( num , 2 )


if __name__ == "__main__":
    main()
