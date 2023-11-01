import logging

class Calculator:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def sum(self, a, b):
        return a + b

    def minus(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return a / b

    def run(self):
        while True:
            a = self.get_value("Enter a: ")
            b = self.get_value("Enter b: ")
            op = self.get_operation()

            if op == "+":
                result = self.sum(a, b)
            elif op == "-":
                result = self.minus(a, b)
            elif op == "*":
                result = self.multiplication(a, b)
            elif op == "/":
                result = self.division(a, b)

            print("Result =", result)
            self.logger.info(f"Operation: {a} {op} {b} = {result}")

            exit_program = input("Do you want to exit the program? (yes/no): ")
            if exit_program.lower() == "yes":
                print("Quitting the program")
                break

    def get_value(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a valid integer")

    def get_operation(self):
        while True:
            op = input("Operation (+, -, *, /): ")
            if op in ("+", "-", "*", "/"):
                return op
            else:
                print("Invalid operation. Please use +, -, *, /")


if __name__ == "__main__":
    logging.basicConfig(filename='calc.log', level=logging.INFO, format='%(asctime)s - %(message)s')
    calculator = Calculator()
    calculator.run()