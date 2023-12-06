import csv
from Student import Student

import csv

class Utils:
    @staticmethod
    def load_data(file_name):
        student_list = []
        with open(file_name) as file:
            reader = csv.DictReader(file)
            for row in reader:
                student_list.append(Student(row["name"], row["phone"], row["age"], row["grade"]))
        return student_list

    @staticmethod
    def save_data(file_name, student_list):
        fieldnames = ["name", "phone", "age", "grade"]

        with open(file_name, "w", newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for student in student_list:
                writer.writerow({"name": student.name, "phone": student.phone, "age": student.age, "grade": student.grade})