import functools
from pympler import asizeof
import time
import math
import random


def timer(func):
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        # Делаем что-то до
        start = time.perf_counter()
        result = func(*args, **kwargs)
        # Делаем что-то после
        runtime = (time.perf_counter() - start) * 1000
        print(f'{func.__name__} took  {runtime:.4f} ms')
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


# Шейкерная сортировка
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


# Сортировка выбором
@timer
def selectionSort(array):
    array = list(array)
    for i in range(len(array)):
        min_idx = i
        for idx in range(i + 1, len(array)):
            if array[idx] < array[min_idx]:
                min_idx = idx
        array[i], array[min_idx] = array[min_idx], array[i]
    return array


# Сортировка вставками
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


# Сортировка Шелла
@timer
def shellSort(array):
    array = list(array)
    n = len(array)
    k = int(math.log2(n))
    interval = 2 ** k - 1
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        k -= 1
        interval = 2 ** k - 1
    return array


# сортировка кучей
def heapify(array, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and array[i] < array[l]:
        largest = l
    if r < n and array[largest] < array[r]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)


@timer
def heapSort(array):
    array = list(array)
    n = len(array)
    for i in range(n // 2, -1, -1):
        heapify(array, n, i)
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    return array


# Сортировка слиянием
def merge(lst1, lst2):
    lst = []
    i = 0
    j = 0
    while i <= len(lst1) - 1 and j <= len(lst2) - 1:
        if lst1[i] < lst2[j]:
            lst.append(lst1[i])
            i += 1
        else:
            lst.append(lst2[j])
            j += 1
    if i > len(lst1) - 1:
        while j <= len(lst2) - 1:
            lst.append(lst2[j])
            j += 1
    else:
        while i <= len(lst1) - 1:
            lst.append(lst1[i])
            i += 1
    return lst


def mergeSort(array):
    array = list(array)
    if len(array) == 1:
        return array
    mid = (len(array) - 1) // 2
    lst1 = mergeSort(array[:mid + 1])
    lst2 = mergeSort(array[mid + 1:])
    array = merge(lst1, lst2)
    return array


@timer
def mergeSort_front(array):
    return mergeSort(array)


def quickSort(array):
    array = list(array)
    if len(array) > 1:
        pivot = array.pop()
        grtr_lst, equal_lst, smlr_lst = [], [pivot], []
        for item in array:
            if item == pivot:
                equal_lst.append(item)
            elif item > pivot:
                grtr_lst.append(item)
            else:
                smlr_lst.append(item)
        return quickSort(smlr_lst) + equal_lst + quickSort(grtr_lst)
    else:
        return array


# Быстрая сортировка
@timer
def quickSort_front(array):
    return quickSort(array)


@timer
def counting_sort(array):
    array = list(array)

    i_lower_bound, upper_bound = min(array), max(array)
    lower_bound = i_lower_bound
    if i_lower_bound < 0:
        lb = abs(i_lower_bound)
        result = [item + lb for item in array]
        lower_bound, upper_bound = min(array), max(array)

    counter_array = [0] * (upper_bound - lower_bound + 1)
    for item in array:
        counter_array[item - lower_bound] += 1
    pos = 0
    for idx, item in enumerate(counter_array):
        num = idx + lower_bound
        for i in range(item):
            array[pos] = num
            pos += 1
    if i_lower_bound < 0:
        lb = abs(i_lower_bound)
        array = [item - lb for item in array]
    return array


nums = [random.randint(0, 100) for i in range(10)]

print('nums', nums)
print(bubbleSort(nums))
print(shaker_sort(nums))
print(selectionSort(nums))
print(insertionSort(nums))
print(shellSort(nums))
print(heapSort(nums))
print(mergeSort_front(nums))
print(quickSort_front(nums))
print(counting_sort(nums))
