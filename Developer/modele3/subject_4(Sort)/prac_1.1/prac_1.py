import functools
import time
import random


def timer(func):
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        #Делаем что-то ДО
        start = time.perf_counter()
        result = func(*args, **kwargs)
        #Делаем что-то ПОСЛЕ
        runtime = (time.perf_counter() - start) * 1000
        print(f'{func.__name__} потребовалось {runtime:.4f} ms')
        return result
    return _wrapper

#сортировка пузырька
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

#шейкерная сортировка(на самостоятельную работу)

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

#сортирвока выбором
@timer
def selectionSort(array):
    array = list(array)
    for i in range(len(array)):
        min_id = i
        for id in range(i + 1, len(array)):
            if array[id] < array[min_id]:
                min_id = id
        array[i], array[min_id] = array[min_id], array[i]
    return array


nums = [random.randint(0, 100) for i in range(10)]

print('nums', nums)
print(bubbleSort(nums))
print('nums', nums)
print(insertionSort(nums))
print('nums', nums)
print(selectionSort(nums))





