import sys

def main():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    try:
        lines = 0
        with open(sys.argv[1]) as file:
            for line in file:
                if line.lstrip().startswith("#") or line.isspace():
                    continue
                lines +=1
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        print(lines)


main()
