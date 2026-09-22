# i = 3
# while ( i > 0 ):
#     print("meow")
#     i -= 1
# for _ in range(132):
#     print("meow")
# print( "meow\n" * 3 , end = "" )
# while True:
#     n = int(input("n: "))
#     if n > 0:
#         break
# for _ in range(n):
#     print("meow")

def main():
    num = getNum()
    meow(num)



def meow(n):
    for _ in range(n):
        print("meow")

def getNum():
    while True:
        n = int(input("n: "))
        if n > 0:
            return n


main()
