from Utils import Utils
import sys

def main():
    if len(sys.argv) != 2:
        print("Python script.py <file_name.csv>")
        sys.exit(1)
    
    file_name = sys.argv[1]
    student_list = Utils.load_data(file_name)

    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match choice:
            case "C" | "c":
                print("New element will be created:")
                list.addNewElement(student_list)
                list.printAllList(student_list)
            case "U" | "u":
                print("Existing element will be updated:")
                list.updateElement(student_list)
                list.printAllList(student_list)
            case "D" | "d":
                print("Element will be deleted")
                list.deleteElement(student_list)
            case "P" | "p":
                print("List will be printed")
                list.printAllList(student_list)
            case "X" | "x":
                print("Exit")
                list.save_data(file_name, student_list)
                break
            case _:
                print("Wrong choice")

if __name__ == "__main__":
    main()
