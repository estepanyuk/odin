#Локальная переменная
'''
def sum():
    a = 10 #Локальная переменная
    b = 20 #Локальная переменная
    c = a + b
    print('Сумма', c)

sum()

def maxmin(x,y):
    if x > y:
        return x
    elif x == y:
        return 'Числа равны'
    else:
        return y

#maxmin(2,3)
print(maxmin(3,5))

def sum():
    c = a + b
    print('Сумма', c)

def sub():
    c = a - b
    print('Разница', c)

#глобальные переменные
a = 10
b = 20

sum()
sub()


c = 10

def mul():
    #глобальная переменная
    global c
    c = c * 10
    print('Значение в функции', c)

mul()
print('Значение вне функции', c)

#nonlocal
def func_outer():
    x = 2
    print('x равно', x)

    def func_inner():
        nonlocal x
        x = 5

    func_inner()
    print('Локальное x сменилось на ', x)

func_outer()


'''
#задача 1

def prod(a, b):
    if a < b:
        return prod(b, a)
    elif b != 0:
        return a + prod(a, b - 1)
    else:
        return 0

x = int(input()) #15
y = int(input()) #10
print(prod(x, y))


"""

def summ(n):
    if n == 1:
        return 1
    return n + summ(n-1)
print(summ(5))


def summ(n):
    x = 0
    for n in range(1, n+1):
        x += n
    return x

print(summ(5))
"""




