#Задача 1
#вариант 1
from random import randint
import random

arr = [random.randint(100, 200) for _ in range(10)]

# Ищем первое число с последней цифрой 2
found = False
for i, num in enumerate(arr):
    if num % 10 == 2:
        print(f"Список: {arr}\n Нашли: A[{i}] = {num}")
        found = True
        break

if not found:
    print(f"список: {arr}\n Не нашли.")

#вариант 2
from random import randint

A = [randint(100, 200) for i in range(10)]
print("Список")
print(A)

for i in range(len(A)):
    if A[i] % 10 == 2:
        print("Нашли: A[", i, "]=", A[i], sep='')
        break
else:
    print("Не нашли")

#вариант 3
import random

# Создаем массив из 10 случайных чисел в диапазоне [100, 200]
c = [random.randint(100, 200) for _ in range(10)]
print(c)

found = False
for num in c:
    if num % 10 == 2:
        print(f"Нашли: {num}")
        found = True
        break

if not found:
    print("Не нашли.")

#вариант 4
import random as r
a = [r.randint(100,200) for i in range(10)]
print(a)
for i in range(10):
    if a[i] % 10 == 2:
        print("Да есть ...","A",i,a[i])
        break
else:
        print("Нету такого числа")

#Задача 2
#вариант 1
import random
a = [random.randint(0,5) for i in range(10)]
b = int(input("Что ищем?"))
print(a)
с = False
for j in range(10):
    if a[j] % 10 == b:
        print(f"А[{j}]={a[j]}")
        с = True
        continue
    else:
        j += 1
    continue
if not с:
    print("Не нашли")

#вариант 2
from random import randint

A = [randint(0, 5) for i in range(10)]
print(A)

x = int(input("Что ищем: "))
isFind = False
for i in range(len(A)):
    if A[i] == x:
        print("A[", i, "]=", A[i], sep="")
        isFind = True

if not(isFind):
    print("Не нашли")

#вариант 3
import random as r
n=int(input('Введи чсило и я дам конфетку'))
a = [r.randint(0,5) for i in range(10)]
b = False
print(a)
for i in range(10):
    if a[i] % 10 == n :
        print('да,такое число есть и оно >>>',i,'<<индекс',a[i])
        b = True

if not b:
    print('Такого числа нету тут')

#вариант 4
import random as r
b = False
a = [r.randint(0,5) for i in range(10)]
print(a)
x = int(input("Введите искомое число:"))
for i in range(10):
    if a[i] == x:
        print("Да есть ...","A",i,a[i])
        b = True
if not b:
    print("Нету такого числа")

#Задача 3
#вариант 1
numbers = ['лучистый', 'лен', 'любовно', 'лепит']
changes = []

for word in numbers:
    if word.startswith('л'):
        modified_word = word[0].upper() + word[1:]
        changes.append(modified_word)
    else:
        changes.append(word)
print('Результат: ', changes)

#вариант 2
b = ["лучистый", "лен", "любовный", "лепит"]

for i in b:
    if i.startswith("л"):
        i = i.capitalize()
    print(i, end=' ')

# вариант 3
a = ["король","книга","керосин","колокол","лента"]
for i in a:
    if i.startswith("к"):
        print(i.replace(i,i.title()))
    else:
        print(i)

# вариант 4
a = ["лучистый", "лен", "любовно", "лепит", "кек"]
for i in a:
    if i.startswith("л"):
        print(i.replace(i, i.title()))
    elif i != i.startswith("л"):
        print(i)