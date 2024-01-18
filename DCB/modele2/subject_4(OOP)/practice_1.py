
class Money():
    # статические поля(переменные объекта)
    rub = 0
    kop = 0

    def __init__(self, rub, kop):
        #динамические поля
        self.rub = rub
        self.kop = kop

    def write(self):
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


    def copm(self, num_rub, num_kop):
        if num_rub > self.rub:
            print(f"{num_rub}, {num_kop}, '>'")
        elif num_rub < self.rub:
            print(f"{num_rub}, {num_kop}, '<'")
        elif num_kop > self.kop:
            print(f"{num_rub}, {num_kop}, '>'")
        elif num_kop < self.kop:
            print(f"{num_rub}, {num_kop}, '<'")
        else:
            print(f"{num_rub}, {num_kop}, '='")


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

obj.copm(20, 63)
obj.write()