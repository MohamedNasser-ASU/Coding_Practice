# students = ["Hermione", "Harry", "Ron"]
# for i in range(len(students)):
#     print(i+1,students[i])

# students = {
#     "Hermione" : "Gryffindor",
#     "Harry" : "Gryffindor",
#     "Ron" : "Gryffindor",
#     "Draco" : "Slytherin",
# }
# for student in students:
#     print(student, students[student], sep = ", ")

students= [
    { "name" : "Hermione", "House" : "Gryffindor", "patronus" : "Otter"},
    { "name" : "Harry", "House" : "Gryffindor", "patronus" : "stag"},
    { "name" : "Ron", "House" : "Gryffindor", "patronus" : "jrt"},
    { "name" : "Draco", "House" : "Slytherin", "patronus" : None }
]
for student in students:
    print(student["name"], student["House"], student["patronus"], sep=", ")
