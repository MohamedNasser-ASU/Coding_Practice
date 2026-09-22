def main():
    prompt = "What's X? "
    x = get_int(prompt)
    print(f"X is {x}")
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            # print("Enter an integer")
            pass
main()


