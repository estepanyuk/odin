#задача 1
#с помощью reduce и лямбда-функции;
from functools import reduce

a = list(map(int, input('Введите целые числа').split()))
print(reduce(lambda x,y: x+y, a))


b = lambda x: x*2
print(b(5))

def b(x):
    return x * 2

print(b(5))

#с math.prod() - возвращает произведение элементов из заданного итерируемого объекта.
import math

a = list(map(int, input("Введите целые числа: ").split(" ")))
print(math.prod(a))

#с использованием пользовательской функции.
def b(x):
    b = 1
    for i in x:
        b *= i
    return b

a = list(map(int, input('Введите целые числа').split()))
print(b(a))

#задача 2
#анонимной функции
banan = input().split()
print(*sorted(list(filter(lambda x: len(x) == 5, banan))))

#с помощью спискового включения
banan = input().split()
print(*sorted([i for i in banan if len(i) == 5]))