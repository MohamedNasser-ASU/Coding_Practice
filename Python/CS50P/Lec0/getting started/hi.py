def main():
    name = input("whats your name? ")
    hello()
    hello(name)

def hello( to = "world" ):
    print(f"Hello, {to}")

main()
