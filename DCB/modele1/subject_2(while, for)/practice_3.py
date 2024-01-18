#Задача 1
#вариант 1
a,b,c,d = map(int, input('Введите число ').split())
print(a + b + c + d)

#вариант 1.1
w = 0
q = list(map(int, input().split()))
for i in range(len(q)):
    w += q[i]
print(w)

#вариант 2
n = int(input())
summary = 0
while n % 10 != 0:
    summary = summary + n % 10
    n = int(n / 10)
print(summary)

#вариант 3
a = int(input("Введите натуральное число: "))  # Запросить пользователя ввести число
b = 0  # Инициализировать переменную для хранения суммы

# Пройтись по каждой цифре в числе и добавить ее к сумме
while a > 0:
    digit = a % 10  # Получить последнюю цифру числа
    b += digit  # Добавить цифру к сумме
    a //= 10  # Удалить последнюю цифру числа

print("Сумма цифр введенного числа:", b)  # Вывести сумму цифр

#вариант 4
b = map(int, input())
a = 0
for i in b:
    a += i
print(a)

#вариант 5
a = int(input('Введите натуральное число:'))
b = 0
for i in str(a):
    b += int(i)

print("Сумма цифр числа", a, "равна", b)

#вариант 6
print(sum(int(i) for i in input()))

#задача 2
#вариант 1
a = int(input())
b = False
while a > 9:
    if a % 10 == a // 10 % 10:
        b = True
        break
    a //= 10
print('Да' if b else 'Нет')

#задача 3
a = int(input())
b = int(input())
for i in range(a,b+1):
     print(i)




