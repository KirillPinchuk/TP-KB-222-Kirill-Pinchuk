import math 
def FindD(a, b, c):
    D =  b**2 - 4 * a * c
    
    if D < 0:
        return "No roots"
    
    elif D == 0:
        x = -b / (2*a)
        return x
    
    else: D > 0
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    return x1, x2
        

a = int(input("Please enter coef a : "))
b = int(input("Please enter coef b : "))
c = int(input("Please enter coef c : "))

roots = FindD(a, b, c)

print("Result:", roots)