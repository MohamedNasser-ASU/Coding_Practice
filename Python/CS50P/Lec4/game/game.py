import random
def main():
    while True:
        try:
            n = int(input("Level: "))
            if n < 1:
                continue
        except ValueError:
            continue
        else:
            while True:
                try:
                    guess = int(input("Guess: "))
                    rand = numGenerator(n)
                    if guess > 1:
                        if guess == rand:
                            print("Just right!")
                            break
                        elif guess > rand:
                            print("Too large!")
                            continue
                        else:
                            print("Too small!")
                            continue
                    else:
                        continue
                except ValueError:
                    continue
            break
def numGenerator(n):
    return random.randint(1,n)
main()
