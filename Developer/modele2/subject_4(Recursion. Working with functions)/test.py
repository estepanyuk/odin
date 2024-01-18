#practice_1
# Задача 1
# вариант 1 с помощью reduce и лямбда-функции;
from functools import reduce

lst = list(map(int, input().split()))
print(reduce(lambda x, y: x * y, lst))

# вариант 2 с math.prod();
import math

lst = list(map(int, input().split()))
print(math.prod(lst))

# вариант 3 с использованием пользовательской функции.
def prod(lst):
    prod = 1
    for i in lst:
        prod *= i
    return prod


lst = list(map(int, input().split()))
print(prod(lst))

# Задача 2
# вариант 1 использованием анонимной функции
my_lst = input().split()
print(*sorted(list(filter(lambda x: len(x) == 5, my_lst))))

# вариант 2 с помощью спискового включения
my_lst = input().split()
print(*sorted([i for i in my_lst if len(i) == 5]))

#practice_2
# Задача 1
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

inter = list(filter(lambda x: x in lst1, lst2))
print('Пересечение:', *intersection)

# Задача 2
lst = list(map(int, input().split()))
print(*sorted(lst, key=lambda i: 0 if i == 0 else -1 / i))

# Задача 3
#Вариант 1 с помощью лямбда-функции;
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

print(*list(map(lambda x, y: x + y, lst1, lst2)))

#Вариант 2 с помощью функции zip() с помощью спискового включения;
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

print(*([i + j for i, j in zip(lst1, lst2)]))

for i, j in zip(lst1, lst2):
    print(i + j, end=' ')

def sumsp(a, b):
    return [i + j for i, j in zip(a, b)]

lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

print(*(sumsp(lst1, lst2)))


# Задача 4 фибоначи
#Вариант 1 простая рекурсия
def fibonacci(x):
    if x in (1, 2):
        return 1
    return fibonacci(x - 1) + fibonacci(x - 2)

n  = int(input('Введите число: '))
print(fibonacci(n))

def fib_recursion(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursion(n-1) + fib_recursion(n-2)

n  = int(input('Введите число: '))
print(fib_recursion(n))

#Вариант 2 с помощью reduce и лямбда-функции;
from functools import reduce

fibonacci = lambda n: reduce(lambda x, n: x + [x[-1] + x[-2]], range(n - 2), [1, 1])
n  = int(input('Введите число: '))
print(*fibonacci(n))

# Задача 5
lst = input().split()
word = input()
print(*list(filter(lambda x: (set(word) == set(x)), lst)))

# Задача 6
# Решение 1 – рекурсивное:
def gcd_recursive(a, b):
    min_num = min(a, b)
    max_num = max(a, b)

    if min_num == 0: #граничный случай, когда одно из чисел равно 0
        return max_num
    elif min_num == 1: #граничный случай, когда одно из чисел равно 1
        return 1
    else: #рекурсивный случай, когда ни одно из чисел не равно ни 1, ни 0
        return gcd_recursive(min_num, max_num % min_num)
a, b = int(input()), int(input())
print(gcd_recursive(a, b))

#Решение 2 – итеративное:

def gcd_iter(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return b

a, b = int(input()), int(input())
print(gcd_iter(a, b))

#Примечание: задачу можно решить с помощью math.gcd():

import math

a, b = int(input()), int(input())
print(math.gcd(a, b))

#practice_3
#задача 1
def check(n):
    if n < 2:
        return n % 2 == 0
    return check(n - 2)

n = int(input("Введите число: "))
print("Число", "четное!" if check(n) else "нечетное!")

#задача 2
def product(a, b):
    if (a < b):
        return product(b, a)
    elif (b != 0):
        return (a + product(a, b-1))
    else:
        return 0
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
print("Произведением двух чисел будет: ", product(a, b))

#задача 3
def sum1(lst):
    total = 0
    for element in lst:
        if (type(element) == type([])):
            total = total + sum1(element)
        else:
            total = total + element
    return total

lst1 = list(map(int, input('Введите числа 1: ').split()))#[1, 2]
lst2 = list(map(int, input('Введите числа 2: ').split()))#[3, 4]

print("Сумма элементов равна:", sum1([lst1,lst2]))

#задача 4
"""

Решение задачи
1. Задаем рекурсивную функцию, которая может принимать в качестве аргумента число и множитель для разряда числа.
2. Принимаем от пользователя число и передаем его в качестве аргумента в рекурсивную функцию.
3. В самой функции в качестве условия рекурсии задаем входящий аргумент больше нуля.
4. При истине в условии вычисляется текущий разряд итогового числа путем нахождения остатка от деления аргумента на 2, 
умноженного на наш множитель разряда числа (по умолчанию 1). 
5. далее мы возвраащем результат нашей фукции как сумму текущего разряда итоговоого числа и функцию которая 
формирует рекурсивное значение
6. далее по условие когда мы доходим до 0, то наша фукция заканчивает работу
"""
#вариант 1
def dec_to_bin(number, rang=1):  # number - число для перевода, rang - множитель для разряда числа
    if number > 0:
        curent_number = (number % 2) * rang # curent_number - текущая цифра
        return curent_number + dec_to_bin(number // 2, rang * 10)
    else:
        return 0

#вариант 2
def dec_to_bin(number, rang=1):
    return (number % 2) * rang + dec_to_bin(number // 2, rang * 10) if number > 0 else 0

n = int(input('Введите десятичное число: '))
print(dec_to_bin(n))


n = int(input('Введите десятичное число: '))
print(dec_to_bin(n))
"""

20/2 = 10(0)
10/2 = 5 (0)
5/2  = 2 (1)
2/2  = 1 (0)
1/2  = 0 (1)

0 * 1 + 0 * 10 + 1 * 100 + 0 * 1000 + 1 * 10000 + 0 = 10100
"""
#задача 5
def check(string, ch):
    if not string:
        return 0
    elif string[0] == ch:
        return 1 + check(string[1:], ch)
    else:
        return check(string[1:], ch)
string = input("Введите строку:")
ch = input("Введите букву для проверки:")
print("Количество вхождений:")
print(check(string, ch))


