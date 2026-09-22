import csv
# take name and home , write them into a .csv the dict way
name = input("What's your name? ")
home = input("What's your house? ")
with open("students.csv", "a") as file:
    writer = csv.DictWriter(file , fieldnames = ["name","home"])
    writer.writerow({"name": name, "home": home})
