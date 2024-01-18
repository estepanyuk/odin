#1 вариант
#a, b, c = map(int, input('Введите возраст Антона, Бориса, Виктора: ').split( ))

a = int(input('Введите возраст Антона '))
b = int(input('Введите возраст Бориса '))
c = int(input('Введите возраст Виктора '))

m = a
if m < b:
    m = b
if m < c:
    m = c
if m == a and m == b and m == c:
    print("Все одного возраста")
elif m == a and m == b:
    print('Антон и Борис старше Виктора')
elif m == a and m == c:
    print('Антон и Виктора старше Борис')
elif m == b and m == c:
    print('Борис и Виктора старше Антона')
elif m == a:
    print("Антон старше всех")
elif m == b:
    print("Борис старше всех")
elif m == c:
    print("Виктор старше всех")

#2 вариант
a = int(input("Введите возраст Антона: "))
b = int(input("Введите возраст Бориса: "))
c = int(input("Введите возраст Виктора: "))
n = max(a, b, c)
if n == a and n == b and n == c:
    print("Все одного возраста.")
elif n == a and n == b:
    print('Антон и Борис старше Виктора.')
elif n == a and n == c:
    print('Антон и Виктор старше Бориса.')
elif n == b and n == c:
    print('Борис и Виктор старше Антона.')
elif a > b and a > c:
    print('Антон старше всех.')
elif b > a and b > c:
    print('Борис старше всех.')
elif c > a and c > b:
    print('Виктор старше всех.')

#3 вариант
a = int(input("Введите возраст Антона"))
b = int(input("Введите возраст Бориса"))
c = int(input("Введите возраст Виктора"))
if a > b and a > c:
    print("Антон старше всех ему", a, "лет")
elif b > a and b > c:
    print("Борис старше всех ему", b, "лет")
elif c > b and c > a:
    print("Виктор старше всех ему", c, "лет")
elif a == b and a == c and b == c:
    print("У всех вораст одинаковый им по", a, "лет")
elif a == b:
    print("Возраст Антона и Бориса одинаковый им по", a, "лет")
elif a == c:
    print("Возраст Антона и Виктора одинаковый им по", a, "лет")
elif b == c:
    print("Возраст Бориса и Виктора одинаковый им по", b, "лет")

#4 вариант
while True:
    a = int(input())
    b = int(input())
    c = int(input())

    if a == b == c:
        print(1)
    elif a > b and a > c:
        print(a)
    elif b > a and b>c:
        print(b)
    elif c > a and c > b:
        print(c)
    else:
        print(11)

#задача 2
a = int(input("Введите число месяца: "))
if a >= 1 and a <= 2 or a == 12:
    print("Зима")
elif a >= 3  and a <= 5:
    print("Весна")
elif a >= 6  and a <= 8:
    print("Лето")
elif a >= 9  and a <= 11:
    print("Осень")
else:
    print("Неверный номер месяца")


#задача 3
# Введите количество секунд
total_seconds = int(input("Введите количество секунд: "))

# Рассчитываем часы, минуты и секунды
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

# Выводим результат
#print(f"Часы: {hours}, Минуты: {minutes}, Секунды: {seconds}")
print(hours, 'ч.', minutes, 'm.',seconds, 'c.',)
