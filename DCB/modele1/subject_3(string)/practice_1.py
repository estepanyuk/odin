#задача 1
"""
a, b = map(int, input("Введите 2 числа: ").split( ))
prod = a * b
print('Произведение', a, 'на', b, 'равно', prod)
print(f'Произведение {a} на {b} равно {prod}')
"""

#задача 2
#вариант 1
a = str(input("Введите ваше слово.."))

if a[::-1].lower() == a.lower():
    print("Полиндром")
else:
    print("Не полиндром")

#вариант 2
slovo = str(input())
a = slovo[::-1]
if slovo == a:
  print("yes")
else:
  print("no")

#вариант 3
a = str(input("Введите слово: "))
reversed_a = a[::-1]
if a == reversed_a:
    print(f"Слово {a} является палиндромом")
else:
    print(f"Слово {a} не является палиндромом")

#вариант 4
my_str = 'мадам'
my_str = my_str.casefold()
rev_str = reversed(my_str)
if list(my_str) == list(rev_str):
    print("Строка является палиндромом")
else:
    print("Строка не является палиндромом")
