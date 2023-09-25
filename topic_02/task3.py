b = int(input("Enter a: "))
a = int(input("Enter b: "))
op = (input("Operation: "))

match op:  
   case "+":
     a + b
     print ("result =", a + b)
     
   case "-":
     a - b 
     print ("result =", a - b) 

   case "*":
    a * b 
    print ("result =", a * b)
    
   case "/":
    a / b
    print ("result =", a / b)