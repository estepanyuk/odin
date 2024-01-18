#Множества- set
#через функцию set()
a = [1,2,3]
a_2 = set(a)
print(type(a_2))

#литеральное
b = {1,2,3,4}
print(type(b))
b.add(5)
print(b)

#Задача 1
#set_a, set_b, set_c = set(input('Введите 1 слово: ')), set(input('Введите 2 слово: ')), set(input('Введите 3 слово: '))
#print('Да' if set_a==set_b==set_c else 'Нет')

A = {1, 2 ,3}
A = set('qwerty')
print(A)

print(1 in A, 4 not in A)
A.add(4)

#Словари - Dict
#key:value

d={
    'alex':'67583765',
    'pavel':'67583765',
    'oleg':'alex@mail.ru',
}
print(d.keys())
print(d.values())
print(d['alex'])
print(d.items())

key = 'alex'
if key in d:
    del d[key]

print(f'удаление {d}')


keys = input('Введите список продуктов ').split()
values = map(int, input('Введите количество ').split())
my_dict = dict(zip(keys, values))
print(my_dict)



