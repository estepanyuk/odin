#1
#Создать 5x5 матрицу со значениями в строках от 0 до 4

import numpy as np

a = np.zeros((5,5), dtype=int)
a += np.arange(5)
print(a)

#2
#Создать 8x8 матрицу и заполнить её в шахматном порядке
a = np.zeros((8,8), dtype=int)
a[1::2,::2] = 1
a[::2,1::2] = 1
print(a)

#3
#Создать вектор размера 10, заполненный нулями, но пятый элемент равен 1
a = np.zeros(10)
a[4] = 1
print(a)

#4
#Создать массив 10x10 со случайными значениями, найти минимум и максимум
a = np.random.random((10,10))
amin, amax = a.max(), a.min()
print(amax, amin)


#5
#Перемножить матрицы 5x3 и 3x2
a = np.dot(np.ones((5,3)), np.ones((3,2)))
print(a)
