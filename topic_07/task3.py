class Calculator:
    def __init__(self, a, b):
        self._a = a
        self._b = b
        self._result = 0
    
    @property 
    def a(self):
        return self._a
    
    @property
    def b(self):
        return self._b
    
    @a.setter
    def a(self, new_a):
             self._a = new_a

        
    @b.setter
    def b(self, new_b):
             self._b = new_b

    @property
    def result(self):
        return self._result

    def add(self):
        self._result = self._a + self._b

    def subtract(self):
        self._result = self._a - self._b

    def multiply(self):
        self._result = self._a * self._b

    def divide(self):
        if self._b == 0:
            self._result = "Error "
        else:
            self._result = self._a / self._b

def get_calculator():
    a = float(input("Enter number a: "))
    b = float(input("Enter number b: "))
    return Calculator(a, b)

def main():
 while True:
    calculator = get_calculator()
    operation = input("Operation (+, -, *, /) ")

    if operation == "+":
        calculator.add()
    elif operation == "-":
        calculator.subtract()
    elif operation == "*":
        calculator.multiply()
    elif operation == "/":
        calculator.divide()
    else:
        print("Invalid operation")
        break

    print("Result =", calculator.result)

if __name__ == "__main__":
    main()
