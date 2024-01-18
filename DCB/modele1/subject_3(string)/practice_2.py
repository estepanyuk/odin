#Задача 1
#Вариант 1
"""
b = ['!','()',"-",'[',']','{','}',';',':','/','<','>','.','?','@','#','$','%','^','&','*','_','~']
a=input('aaaaaaaaaaaaaaaaaaaaaa i oleksei    ')
for i in a:
    if i in b:
        aaaa = a.replace(i,'')
print(aaaa)

#Вариант 2
a = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#b ='Привет!!!, Меня зовут ---Алексей.'
b = input('Введите строку:')
c = ' '
for i in b:
    if i not in a:
        #c = c + i
        c += i
print(c)

#Задача 2
pw = input()
if len(pw) < 6:
    print("Слишком короткий пароль")
else:
    print("ОК!")
"""

#Задача 3
#Вариант 1
a = str(input('Введите пароль от вашего аккаунта стим: '))
if len(a) < 6:
    print('короткий пароль')
elif "qwerty" in a:
    print('слабый')
else:print('норм')

#Вариант 2
a = input()
if len(a)< 6:
    print('пароль короткий')
elif a.startswith('qwerty') :
    print('пароль не подходит')
else:
    print('норм')

#Вариант 3
s = input()
if len(s) < 6:
    print('Короткий пароль!')
if s[0]=='Q' or s[0]=='q'  and s[1]=='W' or s[1]=='w' and s[2]=='E' or s[2]=='e' and s[3]=='R' or s[3]=='r' and s[4]=='T' or s[4]=='t' and s[5]=='Y' or s[5]=='y':
    print('Ненадежный пароль!')
else:
    print("ОК!")

#Задача 4
#Вариант 1
a = input("Введите имя файла: ")
b = "htm"
c = "html"
d = "php"
#print(b, ",", c ,",", d)
b1 = a[-3:]
c1 = a[-4:]
d1 = a[-3:]
if b1==b or c1==c or d1==d:
    print("Это веб-страница!")
else:
    print("Что-то другое.")

# Вариант 2
a = input()
b = "htm"
c = "html"
d = "php"
if b in a or c in a or d in a:
    print("это веб-страница")
else:
    print("это что-то другое")

# Вариант 3
a = input('имя файла: ')
if a.endswith(".htm") or a.endswith(".html") or a.endswith(".php"):
    print("это веб страница!")
else:
    print("что-то другое")

# Вариант 4
name = input('Введите имя файла: ')
if name[-4:] == '.htm' or name[-5:] == '.html' or name[-4:] == '.php':
    print('Это веб-страница!')
else:
    print('Это что-то другое.')
























