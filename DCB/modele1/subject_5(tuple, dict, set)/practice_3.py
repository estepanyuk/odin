#Список [], list
a = [1, 2, 3]
a1 = ['a', 'b', 'c']
a2 = [[1, 2], [[3, 4], [1, 2], [3, 4]]]
print(a2[1][0])
a.append(5)
print(a)
print(len(a2))

b = [3,9,5]
b.sort(reverse=True)
print(b)
b.remove(5)
print(b)

c = '1234567'
k = c.replace('7', '*')
print(k)

#Словарь - {}, dict
#key:value
#задача1.1

key = ('key1', 'key2', 'key3')
value = 0
t = dict.fromkeys(key, value)
print(t)

a = dict.fromkeys([1,2,3,4], [])
a[1].append('qwerty')
print(a)
print(a[2])

b = {key: [] for key in [1,2,3,4]}
print(b)


#задача1.2

key = ['one', 'two', 'three', 'four']
value = [1,2,3,4]
a = {k:v for k,v in zip(key, value)}
print(a)

#списковое включение
sqw = []
for i in (1,2,3,4):
    sqw.append(i*i)
print(sqw)

print([i*i for i in (1,2,3,4)])


#задача1.3
a = {}

a["five"]=5
print(a)

b = {'qwerty':1,'five': 5}
b.update(qwerty=0, blue=5)
print(b)


#задача2
a = input().lower()
my_dict = {i:a.count(i) for i in a}

print(my_dict)
print(*[str(k) + '-' + str(v) for k, v in my_dict.items()])






















