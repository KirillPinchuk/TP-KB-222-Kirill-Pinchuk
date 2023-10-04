while True:
   a = int(input("Enter a: "))
   b = int(input("Enter b: "))
   op = input("Operation: ")

  
   def sum(a, b):
    return a + b
   def minus(a,b):
    return a - b
   def multiplication(a,b):
    return a * b
   def division(a, b):
    if b != 0:
        return a / b
    else:
        print("Division by zero is not allowed")
  

   if op == "+":
    result = sum(a,b)
    break 
    
   elif op == "-":
    result = minus(a,b)
    break 
 
   elif op == "*":
    result = multiplication(a,b)
    break 
 
   elif op == "/":
    result = division(a,b!=0)
    break

print("result =", result)



