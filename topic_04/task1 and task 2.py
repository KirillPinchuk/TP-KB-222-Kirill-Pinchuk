def sum(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Division by zero is not allowed")

def Value(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer")

while True:
    a = Value("Enter a: ")
    b = Value("Enter b: ")
    op = input("Operation (+, -, *, /)")

    if op not in ("+", "-", "*", "/"):
        print("Invalid operation. Please  +, -, *, /")
        continue

    if op == "+":
        result = sum(a, b)
    elif op == "-":
        result = minus(a, b)
    elif op == "*":
        result = multiplication(a, b)
    elif op == "/":
        result = division(a, b)

    print("Result =", result)

    exit = input("Do you want to exit the program? (yes/no): ")
    if exit.lower() == "yes":
        print("Quitting the program")
        break