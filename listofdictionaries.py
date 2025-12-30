# List containing dictionaries
students = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Hermione", "house": "Gryffindor"}
]

# Loop through each dictionary in the list
for student in students:
    # Access values inside each dictionary
    print(student["name"], ",", student["house"])
    
    for stu in student:
         print(stu, ":", student[stu])