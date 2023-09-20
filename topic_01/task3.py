def discriminant(a,b,c):
    D = b*b-4*a*c
    return D
a = int(input("Please enter coef a : "))
b = int(input("Please enter coef b : "))
c = int(input("Please enter coef c : "))
D = discriminant(a,b,c)
result = discriminant(a,b,c)
print(result)