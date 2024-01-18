#задача 1
#вариант 1
list = [[[1, 2], [3, 4]], [[5, 6, 7], [8, 9, 10], [12, 13, 14]]]
a = list[0][0][1]
b = list[1][1][2]
list[0][0].append(11)
print(f"Второй элемент в первом списке первого списка: {a}\nТретий элемент во втором списке второго списка: {b}\nСписок с добавленным числом 11: {list}")

#вариант 2
f = [[[1,2],[3,4]], [[5,6,7],[8,9,10], [12, 13, 14]]]
print(f[0][0][1])
print(f[1][1][2])
f[0][0].append(11)
print(f[0][0][2])
print('baaan')

#задача 2
#вариант 1
numbers = []
numbers.append(1)
numbers.append(2)
numbers.append(3)
print(numbers)
strings = []
strings.insert(0, 'hi')
print(strings)
second_name = numbers[1]
print(second_name)

#вариант 2
numbers = []
numbers.append(1)
numbers.append(2)
numbers.append(3)
print(*numbers)
strings = []
strings.append("Hello")
strings.append("World")
print(*strings)
names = ["Холодильник","Остров","Короли и шут"]
second_name = names[1]
print(second_name)

#задача 3
#вариант 1
Rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
print(Rainbow[0])
Rainbow[0] = 'красный'
print('Выведем радугу')
for i in range(len(Rainbow)):
    print(Rainbow[i])

#вариант 2
import random
a = ['raketa', 'samolet', 'nsok', 'part']
ind = random.randint(0, len(a))
a[ind] = 'kurtka'
print(a)
for i in a:
    print(i)