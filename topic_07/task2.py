class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student_list = [
    Student("Anna", 22),
    Student("Petro", 18),
    Student("Maria", 26),
    Student("John", 36),
    Student("Oleg", 21)
]

sorted_student_list = sorted(student_list, key = lambda student: student.age)
for student in sorted_student_list:
    print(f"Name: {student.name} , age: {student.age}")
     
    