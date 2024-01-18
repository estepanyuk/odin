"""


myStack = []

myStack.append("a")
myStack.append("b")
myStack.append("c")
print(*myStack)

myStack.pop()
print(*myStack)
myStack.pop()
print(*myStack)
myStack.pop()
print(*myStack)
myStack.pop()
print(*myStack)


from collections import deque

myStack = deque()

myStack.append("a")
myStack.append("b")
myStack.append("c")
print(*myStack)

myStack.pop()
print(*myStack)
myStack.pop()
print(*myStack)
myStack.pop()
print(*myStack)
myStack.pop()
print(*myStack)


stack = []
for i in range(1, 11):
    stack.append(f'{i}-й элемент')
    print(f'+ {i}-й элемент добавлен')
    for i in stack:
        print(i, end=" ")
print('\n')
for i in range(len(stack)):
    print('В стеке: ', end=" ")
    for i in stack:
        print(i, end=" ")
    print(f"\n{stack.pop()} удален из стека")



from sys import getrecursionlimit
from sys import setrecursionlimit

print(getrecursionlimit())
setrecursionlimit(2000)
print(getrecursionlimit())

def rec():
    rec()
rec()

#задача 2
#вариант 1
def banan(a):
    print(a)
    if len(a) == 0: #граничный случай
        return
    else:           #рекурсивный случай
        banan(a[:-1])

banan('Hello, world!')

#вариант 2
def banan(a):
    print(a)
    if len(a) > 0: #граничный случай
        banan(a[:-1]) #рекурсивный случай

banan('Hello, world!')
"""

#задача 3
#вариант 1
def num(x):
    if x < 2:
        return x % 2 == 0
    return num(x-2)

check = int(input('Введите целое число: '))
print('Число', 'четное' if num(check) else 'нечетное')

#вариант 2
def abc(n):
    if n == 0:
        return "Число четное!"
    elif n == 1:
        return "Число нечетное!"
    else:
        return abc(n - 2)
number = int(input("Введите число: "))
result = abc(number)
print(result)








