grocery = {}

def main():
    while True:
        try:
            item = input().lower().strip()
        except EOFError:
            output(sorted(grocery.items()))
            break
        else:
            try:
                if item not in grocery:
                    grocery[item] = 1
                else:
                    grocery[item] += 1
            except KeyError:
                pass

def output(grocery):
    for item in grocery:
        print(f"{item[1]} {item[0].upper()}")
main()
