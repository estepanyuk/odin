#1
A =[i+1 for i in range(int(input('')))]
print(A)

#2

X, D, N = map(int, input().split())
A = [X + D * i for i in range(N)]
for i in range(N):
    print(A[i], end=" ")

a = []
for i in range(4):
    a.append(i * i)
print(*a)

a = [i * i for i in range(4)]
print(*a)

#3
from random import randint

A = [randint(100, 200) for i in range(10)]
print(sum(A))
print(sum(A)//len(A))





