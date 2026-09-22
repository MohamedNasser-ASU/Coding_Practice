import csv

# to read a .txt, sort it, then print its content
# with open("names.txt") as file:
#     for line in sorted(file):
#         print("Hi," , line.rstrip())

# to read a .csv, split at ',' then print its content
# with open("names.csv") as file:
#     for line in file:
#         name, place = line.rstrip().split(',')
#         print(f"{name} is from {place}")


# to read a .csv, store its content in a list of dictionaries, sort by key, then print
# persons = []
# # def get_name(person):
# #     return person["name"]
# # will replace this get_name function with lambda function

# with open("names.csv") as file:
#     for line in file:
#         name, place = line.rstrip().split(',')
#         person = {"name": name, "place": place}
#         persons.append(person)
# for person in sorted(persons, key = lambda student: student["name"]):
#     print(f"{person["name"]} is from {person["place"]}")

# use csv.DictReader to read the csv and return dicts, iterate through them and append to persons list then print
persons = []
with open("names.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        persons.append({"name": row["name"], "place": row["place"]})
for person in sorted(persons, key = lambda student: student["name"]):
    print(f"{person["name"]} is from {person["place"]}")
