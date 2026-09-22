def main():

    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):

    if 2 <= len(s) <= 6:
            if s.isalnum():
                if s[0:2].isalpha():
                    for c in s:
                        if c.isdigit():
                            if c == "0":
                                return False
                            else:
                                break
                    for i in range(len(s)-1):
                        if s[i].isdigit() and s[i+1].isalpha():
                            return False
                    return True
                else:
                    return False
            else:
                return False
    else:
        return False


if __name__ == "__main__":
    main()
