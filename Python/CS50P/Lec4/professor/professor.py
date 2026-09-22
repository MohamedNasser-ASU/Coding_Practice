from random import randint

def main():
    numsx = []
    numsy = []
    correct = 0
    level = get_level()
    for _ in range(10):
        numsx.append(generate_integer(level))
        numsy.append(generate_integer(level))
    for i in range(0,10):
        wrong = 0
        for _ in range(3):
            try:
                print(f"{numsx[i]} + {numsy[i]} = ", end = "")
                crct = numsx[i] + numsy[i]
                ans = int(input())
                if ans == crct:
                    correct += 1
                    break
                else:
                    wrong += 1
                    print("EEE")
            except ValueError:
                wrong += 1
                print("EEE")

        if wrong == 3:
            print(f"{numsx[i]} + {numsy[i]} =", (numsx[i] + numsy[i]) )
    print( "Score:" , correct )

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if not ( 0 < level < 4):
                raise ValueError
        except ValueError:
            continue
        else:
            return level


def generate_integer(level):
        if not ( 0 < level < 4):
            raise ValueError
        else:
            if level == 1:
                return randint(0,9)
            elif level == 2:
                return randint(10,99)
            else:
                return randint(100,999)

if __name__ == "__main__":
    main()
