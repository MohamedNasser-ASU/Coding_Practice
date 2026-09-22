months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
def main():
    while True:
        try:
            word = input("Date: ").strip()
            if word[0].isdigit():
                x,y,z = word.split("/")
                try:
                    x,y,z = map(int,(x,y,z))
                except ValueError:
                    continue
                else:
                    if not (1 <= x <= 12 and 1 <= y <= 31):
                        continue
                    else:
                        print(f"{z}-{x:02}-{y:02}")
                        break
            else:
                x,y,z = word.split(" ")
                if x in months:
                    x = months.index(x)+1
                    if y.endswith(","):
                        y = y.rstrip(",")
                    else:
                        continue
                    try:
                        y,z = map(int,(y,z))
                    except ValueError:
                        continue
                    else:
                        if not (1 <= x <= 12 and 1 <= y <= 31):
                            continue
                        else:
                            print(f"{z}-{x:02}-{y:02}")
                            break
                else:
                    continue
        except ValueError:
            continue
main()
