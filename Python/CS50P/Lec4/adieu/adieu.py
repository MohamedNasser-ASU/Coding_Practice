import inflect
p = inflect.engine()
names = []
def main():
    while True:
        try:
            name = input("Name: ")
        except EOFError:
            print()
            print("Adieu, adieu, to" , p.join(names, conj = 'and') )
            break
        else:
            names.append(name)


# p.join(('apples', 'bananas', 'carrots'), conj='and even')
main()
