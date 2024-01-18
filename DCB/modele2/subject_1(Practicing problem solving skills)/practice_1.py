"""
#переменные
#нельзя
#2hello - нельзя писать цифры в начале имени перменной
#2hell o
#знаки +,-
#скобки

#можно
#hello_2
#hello2
#hello
#HelloWorld
#helloWorld
#hello_world

x = 3
y = 4
z = x + y
z = z + 1
x = y
y = 5
x = z + y + 7
print(x)

#Список [], list
a = [1,2,3]
a1 = ['1','2','3']
a2 = [[2,2,0],[[0,2,3],[2,5,1]]]
print(a2[1][1][1])
#a[] += a
#a.list.insert(i,a)
a.append(1)
print(a)
a2.insert(2,3)
print(a2)
print(len(a2))

b = '1234567578385'
c = b.replace('7', '*',1)
print(c)

print(a2[0].count(2))

#кортеж
k = (1,2,3)
y = list(k)
print(y)

a1 = [1,2,3]
print(tuple(a1))


#словарь {}, dict
#key:value
dct = [] - список
dct = () - кортеж
dct = {} - правльный пустой словарь
dct = {None} - не правильно

Dict = {
"Company": "Toyota",
"model": "Premio"
}

Dict[year] = 2012
Dict["year"] = 2012 - правильный вариант
Dict.append("year", 2012)
Dict{"year"} = 2012
print(Dict)

Dict = {"Company": 0,"model": 2}
Dict.update(model=3, model2=5, privet=None)
print(Dict)
Dict1 = {"Company": 0,"model": 2, "privet":None}
Dict1.update(privet=50)
print(Dict1)

print([i*i for i in range(0,10)])

"""














