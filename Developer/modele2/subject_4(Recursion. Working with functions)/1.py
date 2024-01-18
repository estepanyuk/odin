"""
def sum(lst):
    i = 0
    for element in lst:
        if (type(element)) == (type([])):
            i = i + sum(element) # i += sum(element)
        else:
            i = i + element #i += element
    return i

#x = list(map(int, input('Введите числа 1: ').split()))
#y = list(map(int, input('Введите числа 2: ').split()))
#print('Сумма элементов = ', sum([x,y]))

print('Сумма элементов = ', sum([[1, 2],[3, 4],[3, 4]]))



def check(string, buckva):
    if not string:
        return 0
    elif string[0] == buckva:
        return 1 + check(string[1:], buckva)
    else:
        return check(string[1:], buckva)

string, buckva = map(str, input('Введите строку: ').split())
print('Количество вхождений: ', check(string, buckva))
"""