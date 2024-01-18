#задача 1
'''
Напишите программу, которая запрашивает ввод двух значений. Если хотя бы одно из них не является числом,
то должна выполняться конкатенация, то есть соединение, строк. В остальных случаях введенные числа суммируются.

Примеры выполнения программы:

Первое значение: 4
Второе значение: 5
Результат: 9.0
Первое значение: a
Второе значение: 9
Результат: a9
'''
a = input('Первое значение: ')
b = input('Второе значение: ')
try:
    a = float(a)
    b = float(b)
    print('Результат:', a + b)
except ValueError:
    print(str(a) + str(b))
    print(f'Была произведена конкатенация {a} и {b}')
else:
    print(f'Все верно, вы ввели числа {a} и {b}')
finally:
    print('Программа завершена')

#задача 2
'''
Функция plus_two() выполняет одну простую задачу — выводит результат сложения переданного в нее числа 2 и значения 
переменной number. В переменную number должно быть передано число. Обработайте ситуацию, если в эту переменную переданы данные какого-то другого типа. В случае ошибки напечатайте в консоли сообщение «Ожидаемый тип данных — число!».

Запустите код и проверьте работу кода в консоли.

Подсказка:
Используйте конструкцию try/except.В процессе поиска решения попробуйте вывести в консоль сумму строки и числа, изучите сообщение об ошибке.В Python есть специальное исключение для ситуации, если тип переданного значения не соответствует ожиданиям.

Введите число: 2
5
Введите число: цаумк
Ожидаемый тип данных — число!
'''

def plus_two(number):
    # в number ожидается число
    # в ином случае должна выбрасываться ошибка
    try:
        print(2 + number)
    except TypeError:
        print('Ожидаемый тип данных — число!')

plus_two(3)
plus_two("3") 

#задача 2.1

def plus_two(number):
    # в number ожидается число
    # в ином случае должна выбрасываться ошибка
    try:
        print(2 + int(number))
    except ValueError:
        print('Ожидаемый тип данных — число!')


plus_two(input("Введите число: "))

#задача 3
'''
Перед тем как перейти к следующему разделу давайте рассмотрим несколько реальных примеров декораторов. Для того, чтобы определять свои декораторы далее мы будем использовать шаблон кода, который ранее уже последовательно усовершенствовали.

import functools
def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Делаем что-то до
        val = func(*args, **kwargs)
        # Делаем что-то после
        return val
    return wrapper
    
Таймер
Декоратор таймер поможет измерить продолжительность во времени вызовов ваших функций простым и явным способом. 
Следующий пример кода применим для отладке и профайлинге Profiling пользовательских функций.
'''

import functools
import time

def timer(func):
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        runtime = time.perf_counter() - start
        print(f"{func.__name__} took {runtime:.4f} secs")
        return result
    return _wrapper

@timer
def complex_calculation(a, b):
    """Some complex calculation."""
    time.sleep(0.5)
    return a * b

print(complex_calculation(int((input())), (int(input()))))

'''
Видно, что декоратор timer выполняет какой-то код до и после вызова декорируемой функции. 
В остальном же он работает точно так же, как декоратор, 
рассмотренный в предыдущем разделе. Но при его написании мы воспользовались и кое-чем новым.
'''

#задача 4
'''
Применяем сразу несколько декораторов
Вы можете применить несколько декораторов к функции, “накладывая” их друг на друга. 
Давайте определим два простых декоратора и используем их оба для одной целевой функции.
'''
import functools
def greet(func):
    """Приветствуем на английском."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        return "Hello " + val + "!"
    return wrapper
def flare(func):
    """Кое-что добавим в нашу строку."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        return "🎉 " + val + " 🎉"
    return wrapper
@flare
@greet
def getname(name):
    return name
print(getname(input()))

'''
Декораторы выполняются в порядке снизу вверх. Сначала будет выполнен декоратор greet, который применяется к результату, 
возвращенному функцией getname, а затем результат выполнения кода декоратора greet передается коду flare. 
Стек применения декораторов из примера выше может быть в функциональном стиле переписан в следующем виде: flare(greet (getname (name))). 
Самостоятельно измените порядок декораторов и посмотрите, что получится!
'''

#задача 5
'''
Логирование исключений
Точно так же, как в примере с декоратором таймера, мы можем определить декоратор для логирования ошибок выполнения кода, 
который будет регистрировать состояние его выполнения. Для демонстрации его работы я написал логгер, 
вызываемых в ходе выполнения кода исключений, который будет отображать дополнительную информацию: метку текущего времени, 
наименования и значения передаваемых в функцию аргументов.
'''

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
        except Exception as e:
            print("Time: ", datetime.now().strftime("%Y-%m-%d [%H:%M:%S]"))
            print("Arguments: ", sig)
            print("Error:\n")
            raise

    return wrapper


@logexc
def divint(a, b):
    return a / b

print(divint(1, 0))

#задача 6
'''
Напишите функцию-декоратор, которая сохранит (закеширует) значение декорируемой функции. Если декорируемая функция будет вызвана повторно с теми же параметрами — декоратор должен вернуть сохранённый результат, не выполняя функцию.

Подсказка: Создайте словарь и при каждом вызове декоратора сохраняйте в нём аргументы задекорированной функции. При каждом вызове проверяйте, не было ли уже аналогичного вызова. Если был — верните результат прошлого вызова, если не было — верните результат декорируемой функции и одновременно сохраните этот результат в словарь. Ключом для каждой записи словаря может быть аргумент декорируемой функции."
'''
import time
from functools import wraps


def time_check(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        execution_time = round(time.time() - start_time, 1)
        print(f'Время выполнения функции {func.__name__}: {execution_time} с.')
        return result

    return wrapper

cache = {}
def cache_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if args not in cache:
            cache[args] = func(*args, **kwargs)
        return cache[args]
    return wrapper


@time_check
@cache_args
def long_heavy(num):
    time.sleep(1)
    return num * 2


print(long_heavy(1))
# Время выполнения функции long_heavy: 1.0 с.
# 2
print(long_heavy(2))
# Время выполнения функции long_heavy: 0.0 с.
# 2
print(long_heavy(3))
# Время выполнения функции long_heavy: 1.0 с.
# 4
print(long_heavy(4))
# Время выполнения функции long_heavy: 0.0 с.
# 4
print(long_heavy(4))
# Время выполнения функции long_heavy: 0.0 с.
# 4

#задача 7
'''
import requests

res = requests.get('https://ya.ru')
response = requests.request('GET', 'https://ya.ru/get')
print(res.status_code, response.status_code)

print('Получение данный из URL,вывод трассировки')
try:
    response = requests.get('https://ya.ru.ru')
    print(response.status_code)
except Exception as error:
    #Вывести ошибку
    print(error)
else:
    print(response.status_code, response.content)
'''


