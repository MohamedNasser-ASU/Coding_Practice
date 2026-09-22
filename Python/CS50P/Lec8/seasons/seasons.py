import sys
import re
from datetime import date
import inflect
p = inflect.engine()


# today = date.today()
# test = date(2007,6,11)
# diff = today-test
# print(diff.minute)

def main():

    bd = input("Date of Birth: ")
    getBd(bd)
    print(returnMin(getBd(bd)))

def getBd(bd):
    try:
        year, month, day = bd.split('-')
        year = int(year)
        month = int(month)
        day = int(day)
        bd = date(year, month, day)
    except ValueError:
        sys.exit("Invalid date")
    return bd

def returnMin(bd):
    today = date.today()
    diff = today - bd
    diff = diff.days
    minutes = diff * 24 * 60
    output = p.number_to_words(minutes, andword="")
    output = output.capitalize()
    return f"{output} minutes"

if __name__ == "__main__":
    main()
