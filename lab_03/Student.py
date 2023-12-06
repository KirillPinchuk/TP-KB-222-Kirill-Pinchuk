class Student:
    def __init__(self, name, phone, age, grade):
        self.name = name
        self.surname = phone
        self.age = age
        self.phone = grade

    def __str__(self):
        return f"Student name: {self.name}, Student phone: {self.phone}, Student age: {self.age}, Grade: {self.grade}"