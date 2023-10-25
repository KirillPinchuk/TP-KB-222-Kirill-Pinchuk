student_list = [
    {"Name": "Anna", "grade": 85},
    {"Name": "Petro", "grade": 82},
    {"Name": "Maria", "grade": 48},
    {"Name": "John", "grade": 66},
    {"Name": "Oleg", "grade": 95}
]
sorted_grade = sorted(student_list, key = lambda x: x["grade"], reverse = True)
print("Sorting grade:")
for student in sorted_grade:
    print(f"Name: {student['Name']}, Grade: {student['grade']}")

sorted_Name = sorted(student_list, key = lambda x: x["Name"])
print("\nSorting name:")
for student in sorted_Name:
    print(f"Name: {student['Name']}, Grade: {student['grade']}")