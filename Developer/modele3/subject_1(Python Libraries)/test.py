#задача 1
import keyword
#относится ли данная комнада к языку программирования или нет

print(keyword.iskeyword('if'))
print(keyword.iskeyword('List'))
print(keyword.iskeyword('while'))
print(keyword.iskeyword('wolf'))

import copy
#глубокая копия
test_1 = [1, 2, 3, [1, 2, 3]]
test_copy = copy.copy(test_1)
print(test_1, test_copy)

test_copy[3].append(4)
print(test_1, test_copy)

#глубокая копия
test_1 = [1, 2, 3, [1, 2, 3]]
test_deepcopy = copy.deepcopy(test_1)
test_deepcopy[3].append(4)
print(test_1, test_deepcopy)

#задача 2
'''
Заполните массив из 10 элементов случайными числами в интервале [0,5]. Введите число X и найдите все значения, равные X.
Пример:
     Массив: 4, 5, 3, 5, 3, 2, 3, 3, 5, 4
     Что ищем: 2
     2 = [ 5 ]
 Пример:
     Массив: 4, 5, 3, 5, 3, 2, 3, 3, 5, 4
     Что ищем: 6
     Не нашли

import random

a = [random.randint(0, 5) for i in range(10)]
print('Массив: ',*a)

x = int(input('Что ищем: '))
is_find = False
for i in range(10):
    if a[i] == x:
        print(x, '= [', i, ']')
        is_find = True
if not is_find:
    print('Не нашли')
'''

#задача 3
'''
Заполните массив из 10 элементов случайными числами в интервале [0,5]. Найдите пару одинаковых элементов, стоящих рядом. 
Пример:
     Массив: 4 3 2 3 0 3 3 5 1 1
     Что ищем: 3
     3 = [ 5 ] = [ 6 ]
 Пример:
     Массив: 4 3 2 3 0 3 3 5 1 1
     Что ищем: 6
     Не нашли 
     
import random

A = [random.randint(0, 5) for i in range(10)]
print('Массив: ',*A)
a = int(input('Что ищем: '))
is_find = False
for i in range(10):
    if A[i] == a and A[i+1] == a:
        print(a,'= [', i, '] = [', i+1, ']')
        is_find = True
if not is_find:
    print('Не нашли')
'''

#задача 4
import datetime
#1
#Выведем текущую дату и время
t = datetime.datetime.now()
print(t)

a = datetime.datetime(2019, 11, 30, 12, 7, 58, 431007)
print(a)

#2
#Выведем отдельно дату и время:
print('Сегодня {}. Время: {}.'.format(t.date(), t.time()))
#3
#Аналогично извлекаются год, месяц и т.д.:
print("Год {}, месяц {}, день {}, {} ч. {} мин. {} сек.".format(t.year,
                                                          t.month,
                                                          t.day,
                                                          t.hour,
                                                          t.minute,
                                                          t.second))

#4
'''
Модуль datetime также удобен для «ручного» задания дат и автоматизации арифметических 
операций с датами. Узнаем интервал времени между двумя главными датами сюжета 
фильма «Назад в будущее 2»:
'''
today = datetime.datetime(year=1985, month=10, day=26, hour=21, minute=0)
future = datetime.datetime(year=2015, month=10, day=21, hour=19, minute=28)
delta = future-today
print(delta)

'''
Добавление найденной разности к первой дате «возвращает» нас в «будущее»:
'''
print(today + delta)

#задача 5
'''
Узнаем, какое число будет через четыре недели. Для форматирования строк 
в модуле datetime имеется функция strftime() с теми же спецификаторами, что и в модуле time:
'''
today = datetime.datetime.now()
future = today + datetime.timedelta(days=28)
f = '%d.%m.%y'
print(today.strftime('Сегодня: ' + f))
print(future.strftime('Через 28 дней будет: ' + f))

#Задача 6
'''
Если вам важнее оперировать не датами, а неделями, днями недели, месяцами, годами, 
то вам нужен модуль calendar.
Модуль calendar содержит функции для работы с календарем. 
В частности, умеет генерировать строки и HTML для вывода каленадарей месяцев и годов. 
Для наглядности напечатаем календарь на декабрь 2019 года:
'''
import calendar
#1
calendar.prmonth(2019, 12)

'''
Всё хорошо, кроме того, что в заголовке используется шаблон названия месяцев в 
родительном падеже (так он обозначен в указанной выше локали системы). 
Мы можем вручную переобозначить константу именования месяцев:
'''
#2
#пустая строка в списке соответствует нулевому месяцу, первый месяц - январь
month_names = ['', 'январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
calendar.month_name = month_names
calendar.prmonth(2019, 12)

#Или использовать сокращения:

calendar.month_name = calendar.month_abbr
calendar.prmonth(1985, 10)

#Задача 7
'''
При помощи calendar можно не только «рисовать» календари, но и осуществлять итерации 
по их составляющим.
'''
import calendar
free_days = []
for i in range(1, 13):
    c = calendar.monthcalendar(2023, i)
    first_week = c[0]
    third_week = c[2]
    fourth_week = c[3]
    # Если на первой неделе месяца есть четверг, то третий
    # четверг должен быть на третьей неделе. Если нет, то
    # на четвертой
    if first_week[calendar.THURSDAY]:
        free_day = third_week[calendar.THURSDAY]
    else:
        free_day = fourth_week[calendar.THURSDAY]
    s = '{0} {1}'.format(free_day, calendar.month_name[i])
    free_days.append(s)
print(", ".join(free_days))


#самостоятельная работа
#задача1
'''
import random
A = []
B = 0
for i in range(4):
    AA=[]
    for j in range(4):
        r = random.randint(0,100)
        AA.append(r)
        B += r
        print ( "{:4d}".format(r), end = "" )
    print()
    A.append(AA)

srd = B/16
print("среднее:", srd)

a=[]
for x in A:
    aa = []
    for y in x:
        if y >= srd:
            aa.append(255)
        else:
            aa.append(0)
    a.append(aa)

for i in range(4):
    for j in range(4):
        print("{:4d}".format(a[i][j]), end="")
    print()
'''

#задача 3
from datetime import datetime

# создадим даты как строки
ds1 = 'Friday, November 17, 2020'
ds2 = '11/17/20'
ds3 = '11-17-2020'

#задача4
# Конвертируем строки в объекты datetime и сохраним
dt1 = datetime.strptime(ds1, '%A, %B %d, %Y')
dt2 = datetime.strptime(ds2, '%m/%d/%y')
dt3 = datetime.strptime(ds3, '%m-%d-%Y')

print(dt1)
print(dt2)
print(dt3)

#задача5
import datetime

current_date = datetime.datetime.now()
current_date_string = current_date.strftime('%m/%d/%y %H:%M:%S')
print(current_date_string)














