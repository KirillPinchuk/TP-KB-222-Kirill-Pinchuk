import csv
import sys

def load_data(file_name):
    student_list = []
    with open(file_name) as file:
        reader = csv.DictReader(file)
        for row in reader:
            student_list.append({"name": row["name"], "phone": row["phone"], "age": row["age"], "grade": row["grade"]})
    return student_list

def save_data(file_name, student_list):
    fieldnames = ["name", "phone", "age", "grade"]

    with open(file_name, "w", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(student_list)

def printAllList(student_list):
    for student in student_list:
        strForPrint = f"Student name: {student['name']}, Phone: {student['phone']}, Age: {student['age']}, Grade: {student['grade']}"
        print(strForPrint)
    return

def addNewElement(student_list):
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    age = input("Please enter student age:")
    grade = input("Please enter student grade:")
    new_student = {"name": name, "phone": phone, "age": age, "grade": grade}
    insert_position = 0
    for student in student_list:
        if name > student["name"]:
            insert_position += 1
        else:
            break
    student_list.insert(insert_position, new_student)
    print("New element has been added")
    return

def deleteElement(student_list):
    name = input("Please enter name to be deleted: ")
    delete_position = -1
    for student in student_list:
        if name == student["name"]:
            delete_position = student_list.index(student)
            break
    if delete_position == -1:
        print("Element was not found")
    else:
        print("Delete position " + str(delete_position))
        del student_list[delete_position]
    return

def updateElement(student_list):
    name = input("Please enter name to be updated: ")
    delete_position = -1
    for student in student_list:
        if name == student["name"]:
            delete_position = student_list.index(student)
            break
    if delete_position == -1:
        print("Element was not found")
    else:
        print("Delete position " + str(delete_position))
        del student_list[delete_position]
    
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    age = input("Please enter student age:")
    grade = input("Please enter student grade:")
    new_student = {"name": name, "phone": phone, "age": age, "grade": grade}

    insert_position = 0
    for student in student_list:
        if name > student["name"]:
            insert_position += 1
        else:
            break
    student_list.insert(insert_position, new_student)
    print("New element has been added")
    return

def main():
    if len(sys.argv) != 2:
        print("Python script.py <file_name.csv>")
        sys.exit(1)
    
    file_name = sys.argv[1]
    student_list = load_data(file_name)

    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match choice:
            case "C" | "c":
                print("New element will be created:")
                addNewElement(student_list)
                printAllList(student_list)
            case "U" | "u":
                print("Existing element will be updated:")
                updateElement(student_list)
                printAllList(student_list)
            case "D" | "d":
                print("Element will be deleted")
                deleteElement(student_list)
            case "P" | "p":
                print("List will be printed")
                printAllList(student_list)
            case "X" | "x":
                print("Exit")
                save_data(file_name, student_list)
                break
            case _:
                print("Wrong choice")

if __name__ == "__main__":
    main()
