#задача 1
def task(a, b):
    print(f'Первое число {a}')
    print(f'Второе число {b}')
    try:
       print(f'Результат {float(a+b)}')
    except TypeError:
        print(f'Результат', str(a)+str(b))
    except ZeroDivisionError:
        print(f'Вы не можите разделить на ноль')
    except:
        print(f'Что-то пошло не так')


    else:
        print(f'Все хорошо, вы ввели числа!')
    finally:
        print('Конец')


task(5, 4)
task(5, "a")


try:
    print(1/0)
except ZeroDivisionError:
    print(f'Вы не можите разделить на ноль')
finally:
    print('Хорошо')


print(1/0)

#задача 2
import time
import functools
def banana(func):
    @functools.wraps(func)
    def snoopy(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        #print('Функция выполнилрось', round(end-start, 2))
        print(f"Функция {func.__name__} выполнилрось", round(end-start, 2))
    return snoopy

@banana
def perf(a, b, c):
    time.sleep(0.5)
    print(a*b*c)

perf(12, 15, 10)

