def Value(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer")
def get_operation():
    while True:
        op = input("Operation (+, -, *, /): ")
        if op in ("+", "-", "*", "/"):
            return op
        else:
            print("Invalid operation. Please  +, -, *, /")