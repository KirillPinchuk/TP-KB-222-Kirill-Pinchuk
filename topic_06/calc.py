import functions
import operations
import logging



logging.basicConfig(filename='calc.log', level=logging.INFO, format='%(asctime)s - %(message)s')

while True:
    a = operations.Value("Enter a: ")
    b = operations.Value("Enter b: ")
    op = operations.get_operation() 
    
    


    if op == "+":
        result = functions.sum(a, b)
    elif op == "-":
        result = functions.minus(a, b)
    elif op == "*":
        result = functions.multiplication(a, b)
    elif op == "/":
        result = functions.division(a, b)

    print("Result =", result)
    logging.info(f"Operation: {a} {op} {b} = {result}")
    

    exit = input("Do you want to exit the program? (yes/no): ")
    if exit.lower() == "yes":
        print("Quitting the program")
        break

    

