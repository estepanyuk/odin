# задача 1
'''
import keyword

print(keyword.kwlist)
print(keyword.iskeyword('List'))

#Реализуйте Поверхностную копию: Необходимо создать новый составной объект(список), и затем (по мере возможности) внести в него ссылки на объекты, находящиеся в оригинале.
#Реализуйте Глубокую копию:  Необходимо создать новый составной объект, и затем рекурсивно внести в него копии объектов, находящихся в оригинале.
'''

#2
import copy

# Поверхностную копию
a = [1, 2, 3, [1, 2, 3]]
a_copy = copy.copy(a)
print(a, a_copy)

a_copy[3].append(4)
print('Поверхностную копию', a, a_copy)

# глубокая копия
a = [1, 2, 3, [1, 2, 3]]
a_deepcopy = copy.deepcopy(a)
a_deepcopy[3].append(4)
print('глубокая копия', a, a_deepcopy)


#задача 2
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

import random as rand
a=[rand.randint(0,5) for _ in range(10)]
print(a)
hz=int(input('Что ищем?'))
ans=[]
for i in range(10):
    if hz==a[i]:
        ans.append(i)
if len(ans)!=0:
    print(hz,' = ', ans)
else:
    print('Не нашли')

#задача 3
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


#задача 4
import datetime
a = datetime.datetime.now()

print('Сегодня {}. Время {}.'.format(a.date(), a.time()))


import datetime
a = datetime.datetime(2015, 10, 21, 19, 28)
b = datetime.timedelta(1985, 10, 26, 21, 0)
print(a-b)

a = datetime.datetime(year=2015, month=10, day=21, hour=19, minute=28)
b = datetime.datetime(year=1985, month=10, day=26, hour=21, minute=0)
print(a-b)

#задача 5

import datetime

today = datetime.datetime.now()
future = today + datetime.timedelta(days=28)

format = '%d.%m.%y'

print(today.strftime('сегодня ' + format))
print(future.strftime('через 28 дней ' + format))

#задача 6
from pytz import timezone
from datetime import datetime

america_time = timezone('America/Los_Angeles')
usa = datetime.now(america_time)
print(usa)

#задача 7
import calendar

#a = calendar.calendar(2023)
#print(a)

calendar.prmonth(2019, 1)

m_name = ['', 'Янв', 'Фев']
calendar.month_name = m_name
calendar.prmonth(2023, 1)

calendar.month_name = calendar.month_abbr
calendar.prmonth(2023, 1)












