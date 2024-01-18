"""



#1 задача
print('Введите три числа')
a = int(input('Введите первое число' ))
b = int(input('Введите второе число' ))
c = int(input('Введите третье число' ))
d = a+b+c
e = a*b*c
f = 3
g = (a+b+c)/f
print(a,"+",b,"+",c,"=",d)
print(a,"*",b,"*",c,"=",d)
print("(",a,"+",b,"+",c,")", "/",f,"=",g)
"""
#2 задача
a, b, c, d = map(int, input("введите четыре числа").split(","))
if a > b and a > c and a > d:
    print("наибольшее число равно", a)
elif b > a and b > c and b > d:
    print("наибольшее число равно",b)
elif c > a and c > b and c > d:
    print("наибольшее число равно", c)
else:
    print("наибольшее число равно", d)

a, b, c, d = map(int, input("Введите 4 числа").split())
print(max(a, b, c, d))



