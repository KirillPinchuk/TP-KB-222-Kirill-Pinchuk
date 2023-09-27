a = int(input("Enter a: "))
b = int(input("Enter b: "))
op = (input("Operation: "))
match op:
   
    case "+":
     def sum(a, b):
      return a + b
     print (a + b)

    case "-":
     def minus(a,b):
      return a - b
     print (a -b)
     
    case "*":
     def multiplication(a,b):
      return a * b
     print (a * b)
      
    case "/":
     if b != 0:
      def division(a, b):
        return a / b
      result = division(a, b)
      print(result)
     else:
       print("Invalid operation")
      
    
    
    

      