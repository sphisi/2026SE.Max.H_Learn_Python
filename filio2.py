import csv

students = []

with open("names.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row[], "job": row1]})


for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is a {student['job']}")