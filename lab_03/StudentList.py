from Student import Student

class StudentList:
    def __init__(self):
        self.students = []

    def __str__(self):
        return '\n'.join(str(student) for student in self.students)

    def add_new_element(self):
        name = input("Please enter student name: ")
        phone = input("Please enter student phone: ")
        age = input("Please enter student age: ")
        grade = input("Please enter student grade: ")
        new_student = Student(name, phone, age, grade)
        
        insert_position = 0
        for student in self.students:
            if name > student.name:
                insert_position += 1
            else:
                break

        self.students.insert(insert_position, new_student)
        print("New element has been added")

    def delete_element(self):
        name = input("Please enter name to be deleted: ")
        for student in self.students:
            if name == student.name:
                self.students.remove(student)
                print(f"{name} has been deleted")
                return
        print("Element was not found")

    def update_element(self):
        name = input("Please enter name to be updated: ")
        for student in self.students:
            if name == student.name:
                self.students.remove(student)
                new_name = input("Enter new name: ")
                new_phone = input("Enter new phone: ")
                new_age = input("Enter new age: ")
                new_grade = input("Enter new grade: ")
                updated_student = Student(new_name, new_phone, new_age, new_grade)
                insert_position = 0
                for s in self.students:
                    if new_name > s.name:
                        insert_position += 1
                    else:
                        break
                self.students.insert(insert_position, updated_student)
                print("Element has been updated")
                return
        print("Element was not found")

    