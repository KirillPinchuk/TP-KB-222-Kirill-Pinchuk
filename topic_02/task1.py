a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
def discr(a, b, c):
    D = b**2 - 4 * a * c
    return D

D = discr(a, b, c)

if D > 0:
    result =  "D more 0"
    print(D)
elif D == 0:
    result = "D equal 0 "
else:
    result = "No solution"

print(result)