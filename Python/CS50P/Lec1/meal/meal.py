def main():

    time = input("What time is it? ").strip()

    if 7.0 <= convert(time) <= 8.0:
        print("breakfast time")
    elif 12.0 <= convert(time) <= 13.0:
        print("lunch time")
    elif 18.0 <= convert(time) <= 19.0:
        print("dinner time")


def convert(time):

    hrs, mins = time.split(":")
    hrs = int(hrs)
    mins = int(mins)
    mins = float(mins/60)
    return float(hrs+mins)


if __name__ == "__main__":
    main()
