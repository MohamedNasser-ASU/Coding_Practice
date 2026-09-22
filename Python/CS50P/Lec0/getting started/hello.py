# name = input("What's your name? ")
# print("Hello,"+ name)
# print("Hello,", end=" ")
# print(name)
# print("Hello,", name , name , sep=" sep " )
# print("Hello, \"world\"" )
# print('Hello, "world"' )

"""
FINALLY , to print hello name do this
"""
# take input , strip and capitalize
name = input("What's your name? ").strip().title()
# print
print(f"Hello, {name}")
# split into first and last
first, last = name.split(" ")
print(f"Hello, {first} {last}")
