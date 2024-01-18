#задача 1
'''
Реализуйте класс Деньги для работы с денежными суммами. Число должно быть представлено двумя полями: для рублей и для копеек.  Дробная часть (копейки)
при выводе на экран должна быть отделена от целой части запятой. В основном коде программы создать экземпляр класса и проверить все методы класса.
Необходимо реализовать следующие методы:
Конструктор (2 аргумента - рубли и копейки)
Сложение (2 аргумента - рубли и копейки)
Вычитание (2 аргумента - рубли и копейки)
Деление (1 аргумент - множитель)
Умножение (1 аргумент - делитель)
Операция сравнения (2 аргумента - рубли и копейки)
Вывод суммы на экран (0 аргументов, формат вывода - 12,34 р)
'''

class Money:
    #статические поля(переменные объекта)
    rub = 0
    kop = 0

    def __init__(self, rub, kop):
        #динамические поля(переменные объекта)
        self.rub = rub
        self.kop = kop

    def write(self):
        #вывод результата Дробная часть (копейки) при выводе на экран должна быть отделена от целой части запятой.
        print('$', int(self.rub),',', int(self.kop), sep='')

    def summ(self, rub, kop):
        self.rub += rub
        self.kop += kop
        self.rub += self.kop // 100
        self.kop %= 100
        print('+$', rub,',', kop, sep='')

    def proz(self, number):
        self.rub *= number
        self.kop *= number
        self.rub += self.kop // 100
        self.kop %= 100
        print('*', number, sep='')

    def minus(self, rub, kop):
        self.rub -= rub
        self.kop -= kop
        self.rub += self.kop // 100
        self.kop %= 100
        print('-$', rub,',', kop, sep='')

    def div(self, number):
        self.rub /= number
        self.kop /= number
        self.kop += (self.rub % 1) * 100 // 1
        self.rub //= 1
        print('/', number, sep='')

    def comp(self, num_rub, num_kop):
        if num_rub > self.rub:
            print(f'{num_rub}, {num_kop}', '>')
        elif num_rub < self.rub:
            print(f'{num_rub}, {num_kop}', '<')
        elif num_kop > self.kop:
            print(f'{num_rub}, {num_kop}', '>')
        elif num_kop < self.kop:
            print(f'{num_rub}, {num_kop}', '<')
        else:
            print(f'{num_rub}, {num_kop}', '=')


obj = Money(12, 50)
obj.write()

obj.summ(13, 70)
obj.write()

obj.proz(3)
obj.write()

obj.minus(13, 70)
obj.write()

obj.div(3)
obj.write()

obj.comp(21, 64)
obj.write()





