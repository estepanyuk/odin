"""
#задача 1
nums = map(int, input().split())
my_dict = {i: 'четное' for i in nums if i % 2 == 0}
print(my_dict)

#задача 2
#k - ключ
#v - значение
#str(k) + '-' + str(v) key - value
st = input().lower()
my_dict = {i: st.count(i) for i in st}
print(*[str(k) + '-' + str(v) for k, v in my_dict.items()])
"""
#задача 3
ct1, ct2 = input().lower(), input().lower()
c = {k: ct1.count(k) for k in ct1}
d = {k: ct2.count(k) for k in ct2}
print('Да' if c == d else 'Нет')