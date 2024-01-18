#задача 1

def task(a,b):
    print(f'First value {a}')
    print(f'Second value {b}')
    try:
        print(f'Result {float(a+b)}')
    except TypeError:
        print('Result',str(a)+str(b))
    else:
        print('Вы ввели числа')
    finally:
        print('Конец')

task(5,2)
task(5,'a')


#задача 2

def plus_two(b):
    try:
        print(2+int(b))
    except ValueError:
        print('Ожидаемый тип данных - число!')

plus_two(input('Введите число: '))

import sys
def decorator(func):
    def start(*args, **kwargs):
        func(*args, **kwargs)
        sys.stdout.write(str("Обращайтесь"))
        return func
    return start

@decorator
def n_out(a):
    try:
        print(int(a) + 2)
    except ValueError:
        print("Неправильное число")
n_out(input("Введите число: "))


#задача 3

import time

def perf_counter(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Функция выполнялась", round(end - start, 2))
    return wrapper

@perf_counter
def perf():
    time.sleep(0.5)

perf()


import time

def decorator(func):
    def inner(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        print(f'Execution time: {end-start}')
    return inner

@decorator
def multiply(a,b):
    time.sleep(0.5)
    print(a*b)

multiply(5213214125411241254125,10003213124100000)

import sys
from time import sleep, perf_counter
def decorator(func):
    def start(*args, **kwargs):
        st = perf_counter()
        sys.stdout.write(str("Perf_counter has been started \n"))
        sleep(1)
        func(*args, **kwargs)
        end = perf_counter() - st - 1
        print(F"Итоговое время: {end} ")
        sys.stdout.write(str("Обращайтесь"))
        return func
    return start
@decorator
def n_out(a, b):
    try:
        print(F" a * b = {float(a)*float(b)}")
    except ValueError:
        print("Неправильно ввели число")

n_out(input("Введите число 1: "), input("Введите число 2: "))

import functools
import time

def timer(func):
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        # Делаем что-то до
        start = time.perf_counter()
        result = func(*args, **kwargs)
        # Делаем что-то после
        runtime = time.perf_counter() - start
        print(f'{func.__name__} took  {runtime:.4f} sec')
        return result
    return _wrapper

@timer
def calc(a,b):
    time.sleep(0.5)
    return a * b

print(calc(3, 5))

'''
#задача 4
'''
def first_decorator(func):
    def wrapper(*args, **kwargs):
        print("Я - первый декоратор.")
        result = func()
        print("Я - первый декоратор, но после выполнения")
        return result
    return wrapper

def second_decorator(func):
    def wrapper(*args, **kwargs):
        print("Я - второй декоратор.")
        result = func()
        print("Я - второй декоратор, но после выполнения")
        return result
    return wrapper

@first_decorator
@second_decorator
def function_to_decorate():
    print("Я функция.")

function_to_decorate()


import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Делаем что-то до
        val = func(*args, **kwargs)
        # Делаем что-то после
        return 'Hello ' + val + '!'
    return wrapper

def flare(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Делаем что-то до
        val = func(*args, **kwargs)
        # Делаем что-то после
        return '😎' + val + '😎'
    return wrapper

@flare
@decorator
def getname(name):
    return name

print(getname('Alex'))

#задача 5
import datetime

def logging(func):
    def logger(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            return res
        except Exception as e:
            now_time = datetime.datetime.now()
            print(f"time: {now_time}\n Arguments: {args}\n Error: {e}")
    return logger
@logging
def calc(a,b):
    print(a/b)

calc(1,5)
calc(1,0)


import functools
from datetime import datetime

def logexc(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        # Преобразуем в строку имена аргументов и их значения
        args_rep = [repr(arg) for arg in args]
        kwargs_rep = [f"{k}={v!r}" for k, v in kwargs.items()]
        sig = ", ".join(args_rep + kwargs_rep)

        # Определяем блок Try для кода, который будем логировать
        try:
            return func(*args, **kwargs)
        except Exception:
            print("Time: ", datetime.now().strftime("%Y-%m-%d [%H:%M:%S]"))
            print("Arguments: ", sig)
            print("Error:\n")
            raise

    return wrapper

@logexc
def divint(a, b):
    return a / b

print(divint(1, 5))








