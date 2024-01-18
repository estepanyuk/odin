#задача 1
#вариант 1
"""
a, b = map(str, input().split(' '))
print(b, a)


#вариант 2
a = input()
first_word = a[:a.find(' ')]
second_word = a[a.find(' ') + 1:]
print(second_word + ' ' + first_word)

#вариант 3
text = input("Введите текст")
word1, word2 = text.split()
print(word2, word1)
"""

#задача 2
#вариант 1
a = "Привет, это пример строки в алфавитном порядке"
aaaa = [i.lower() for i in a.split()]
aaaa.sort()
for i in aaaa:
    print(i)
