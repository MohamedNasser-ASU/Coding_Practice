import re
def main():
    print(convert(input("Hours: ")))
def convert(s):
    x = y = z = q = 0
    # group 1 = first hr, group 2 = first mins, group 3 = AM/PM,
    # group 4 = second hr, group 5 second mins, group 6 = AM/PM,
    matches = re.search(r"^(1?[0-9])(?::([0-5][0-9]))? (AM|PM) to (1?[0-9])(?::([0-5][0-9]))? (AM|PM)$", s, re.IGNORECASE)

    if matches:
        # handle starting time
        hr1 = int(matches.group(1))
        time1 = matches.group(3)
        if time1 == "AM":
            if hr1 != 12:
                x = hr1
            else:
                x = 0
        elif time1 == "PM":
            if hr1 != 12:
                x = hr1 + 12
            else:
                x = hr1

        # handle finishing time
        hr2 = int(matches.group(4))
        time2 = matches.group(6)
        if time2 == "AM":
            if hr2 != 12:
                z = hr2
            else:
                z = 0
        elif time2 == "PM":
            if hr2 != 12:
                z = hr2 + 12
            else:
                z = hr2

        # handle minutes
        if matches.group(2):
            y = int(matches.group(2))
        else:
            y = 0
        if matches.group(5):
            q = int(matches.group(5))
        else:
            q = 0

        return f"{x:02}:{y:02} to {z:02}:{q:02}"
    else:
        raise ValueError

if __name__ == "__main__":
    main()
