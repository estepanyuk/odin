#задача 1
#вариант 1
b = int(input(" Введите количество повторений"))
i = 0
while i < b:
    print("Привет")
    i += 1

# вариант 2
message = int(input("Введите ваше сообщение: "))
repeat = int(input("Введите количество повторений: "))

for i in range(repeat):
    print(message)


# вариант 3
import random

a = random.randint(1,10)
b = 0
while b < a:
    print('Привет')
    b += 1

#задача 2
#s = "Hi, loop"
a = "Hi, oop"
for i in a:
    if i == "l":
        break
    print(i)
else:
    print("Цикл завершен")

#задача 3
for i in range(1,11):
    if i % 2 != 0 and i % 3 != 0:
        print(i)


#задача 4
#вариант 1
for i in range(5):
    print("* * * *")

#вариант 2
n = int(input('Введите число '))
m = int(input('Введите число '))
for i in range(n):
    for j in range(m):
        print("*", end="")
    print()



