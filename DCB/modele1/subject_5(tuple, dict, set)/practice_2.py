#Кортеж - (), Tuple

from sys import getsizeof as g

a = (1,2,3,4,5) #Кортеж
b = [1,2,3,4,5] #Список

print(g(a))
print(g(b))

#задача 1
#варианта 1
a = input("Введите числа через пробел: ").split()
c = f = 0
for num in a:
    if int(num) > 0:
      c += 1
    elif int(num) < 0:
      f += 1
print(f"Положительных чисел: {c}")
print(f"Отрицательных чисел: {f}")

#варианта 2
from random import randint

r = [randint(-50, 50) for i in range(10)]
print(r)
pos = tuple(i for i in r if i > 0)
neg = tuple(i for i in r if i < 0)
print(f'Кортеж {pos} состоит из {len(pos)} положительных чисел')
print(f'Кортеж {neg} состоит из {len(neg)} положительных чисел')

#задача 2
#варианта 1
numbers = ((5, 4, 5, 4), (3, 3, 4, 6), (8, 9, 5, 4), (12, 4, 5, 1), (9, 3, 5, 1))
avg = tuple(sum(i)/len(i) for i in numbers)
print(*avg)

#Множества
#задача 1
hobbi1 = input('Введите хобби 1: ').split()
hobbi2 = input('Введите хобби 2: ').split()
result = len(set(hobbi1) & set(hobbi2)) / float(len(set(hobbi1) | set(hobbi2))) * 100
print(f'{result: .2f}%')

a = set('1234')
b = set('3456')
print(a)
print(b)
print(a|b)
print(a&b)
print(b-a)
print(a^b)


