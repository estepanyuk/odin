'''
# Метод пузырька
#1
from random import randint

li = [randint(0, 50) for i in range(20)]
print("было ", li)

for i in range(1, len(li)):  # Перебираем лист с первого элемента до конца (нумерация с 0) [1, 2, ... , 19]
    for j in range(len(li) - i):  # Перебираем лист с нулевого элемента до конца - i, копим наибольшие в конце [0, 1, ..., 19], [0, 1, ..., 18], ... , [0]
        if li[j] > li[j + 1]:  # Если текущее число больше следующего,
            li[j], li[j + 1] = li[j + 1], li[j]  # то меняем местами, пока наибольшее не встанет в конец

print("стало", li)

#2
from random import randint

li = [randint(0, 50) for i in range(20)]
print("было ", li)

for i in range(1, len(li)):
    n = 0
    for j in range(len(li) - i):
        if li[j] > li[j + 1]:
            li[j], li[j + 1] = li[j + 1], li[j]
            n += 1
    if n == 0:
        print('На шаге', i, 'цикл завершается')
        break

print("стало", li)

#3
from random import randint

def sum_of_nums(num):
    s = 0
    while num != 0:
        s += num % 10
        num = num // 10
    return s

li = [randint(0, 50) for i in range(20)]
print("было ", li)

for i in range(1, len(li)):
    for j in range(len(li) - i):
        if sum_of_nums(li[j]) < sum_of_nums(li[j + 1]):
            li[j], li[j + 1] = li[j + 1], li[j]

print("стало", li)

#Метод выбора (минимального элемента)
#0
from random import randint

li = [randint(0, 50) for i in range(20)]
print("было ", li)

for i in range(len(li) - 1):  # Перебираем лист с нулевого элемента до предпоследнего [0, 1, ... , 18]
    n_min = i  # Предполагаем, что минимальный элемент под номером i
    for j in range(i+1, len(li)):  # Перебираем лист с i+1 элемента до конца [1, 2, ... , 19], [2, 3, ..., 19], ... , [19]
        if li[j] < li[n_min]:  # Если текущее число меньше минимума,
            n_min = j  # то обновляем номер минимального
    if i != n_min:  # Если обновили номер,
        li[i], li[n_min] = li[n_min], li[i] # то меняем местами


print("стало", li)

# 1
from random import randint

li = [randint(0, 50) for i in range(10)]
print("было ", li)

for i in range(len(li) // 2 - 1):
    n_min = i
    for j in range(i+1, len(li) // 2):
        if li[j] < li[n_min]:
            n_min = j
    if i != n_min:
        li[i], li[n_min] = li[n_min], li[i]

for i in range(len(li) // 2, len(li) - 1):
    n_max = i
    for j in range(i+1, len(li)):
        if li[j] > li[n_max]:
            n_max = j
    if i != n_max:
        li[i], li[n_max] = li[n_max], li[i]

print("стало", li)
'''
#«быстрая сортировка» (QuickSort)
#пример работы алгоритма
def quicksort(nums, fst, lst):
    if fst >= lst: return

    i, j = fst, lst
    pivot = nums[(fst + lst) // 2]

    while i <= j:
        while nums[i] < pivot: i += 1
        while nums[j] > pivot: j -= 1
        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1
    quicksort(nums, fst, j)
    quicksort(nums, i, lst)

from random import randint

li = [randint(0, 50) for i in range(20)]
print("было ", li)

quicksort(li, 0, len(li)-1)
print("стало", li)

#1
def quicksort(nums, fst, lst):
    if fst >= lst: return

    i, j = fst, lst
    pivot = nums[(fst + lst) // 2]

    while i <= j:
        while nums[i] < pivot: i += 1
        while nums[j] > pivot: j -= 1
        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1
    quicksort(nums, fst, j)
    quicksort(nums, i, lst)

from random import randint

li = [randint(0, 50) for i in range(20)]
print("было ", li)

quicksort(li, 0, len(li) // 2 - 1)
quicksort(li, len(li) // 2, len(li) - 1)

print("стало", li)