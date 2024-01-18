import functools
import math
import time
import random

def timer(func):
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        # Делаем что-то до
        start = time.perf_counter()
        result = func(*args, **kwargs)
        # Делаем что-то после
        runtime = (time.perf_counter() - start) * 1000
        print(f'{func.__name__} потребовалось  {runtime:.4f} ms')
        return result

    return _wrapper

# Сортировка методом пузырька
@timer
def bubbleSort(array):
    array = list(array)
    swapped = False
    for i in range(len(array) - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if swapped:
            swapped = False
        else:
            break
    return array


#шейкерная сортиртивка
@timer
def shaker_sort(array):
    array = list(array)
    length = len(array)
    swapped = True
    start_index = 0
    end_index = length - 1

    while swapped:
        swapped = False

        # проход слева направо
        for i in range(start_index, end_index):
            if array[i] > array[i + 1]:
                # обмен элементов
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

        # если не было обменов прерываем цикл
        if not swapped:
            break
        swapped = False
        end_index = end_index - 1

        # проход справа налево
        for i in range(end_index - 1, start_index - 1, -1):
            if array[i] > array[i + 1]:
                # обмен элементов
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
        start_index = start_index + 1
    return array

#сортировка выбором
@timer
def selectionSort(array):
    array = list(array)
    for i in range(len(array)):
        min_inx = i
        for idx in range(i + 1, len(array)):
            if array[idx] < array[min_inx]:
                min_inx = idx
        array[i], array[min_inx] = array[min_inx], array[i]
    return array

#сортирвока вставками
@timer
def insertionSort(array):
    array = list(array)
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while array[j] > key and j >= 0:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

#сортировка Шелла
@timer
def shellSort(array):
    array = list(array)
    n = len(array)
    k = int(math.log2(n))
    interval = 2 ** k - 1
    while interval > 0:
        for i in range(interval, n):
            a = array[i]
            j = i
            while j >= interval and array[j - interval] > a:
                array[j] = array[j - interval]
                j -= interval
            array[j] = a
        k -= 1
        interval = 2 ** k - 1
    return array



nums = [random.randint(0, 100) for i in range(10)]

print('nums', nums)
print(bubbleSort(nums))
print('nums', nums)
print(shaker_sort(nums))
print('nums', nums)
print(selectionSort(nums))
print('nums', nums)
print(insertionSort(nums))
print('nums', nums)
print(shellSort(nums))

