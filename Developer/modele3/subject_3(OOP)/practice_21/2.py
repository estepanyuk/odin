from abc import ABC, abstractmethod

class Hen(ABC):
    @abstractmethod
    def getCountOfEggsPerMonth(self):
        pass

    def getDescription(self):
        return 'Я курица!'

#RussianHen, MoldovanHen, BelarusianHen

class RussianHen(Hen):
    def getCountOfEggsPerMonth(self):
        return 100

    def getDescription(self):
        return Hen.getDescription(self) + 'Моя страна-Россия. Я несу ' + str(self.getCountOfEggsPerMonth()) + ' яиц в месяц'

class MoldovanHen(Hen):
    def getCountOfEggsPerMonth(self):
        return 55

    def getDescription(self):
        return Hen.getDescription(self) + 'Моя страна-Молдова. Я несу ' + str(self.getCountOfEggsPerMonth()) + ' яиц в месяц'

class BelarusianHen(Hen):
    def getCountOfEggsPerMonth(self):
        return 90

    def getDescription(self):
        return Hen.getDescription(self) + 'Моя страна-Белоруссия. Я несу ' + str(self.getCountOfEggsPerMonth()) + ' яиц в месяц'


class HenFactory:
    def getHen(self, country):
        if country == 'rus':
            return RussianHen()
        elif country == 'mol':
            return MoldovanHen()
        elif country == 'bel':
            return BelarusianHen()

fabrica = HenFactory()

hen1 = fabrica.getHen('rus')
print(hen1.getDescription())

hen1 = fabrica.getHen('mol')
print(hen1.getDescription())

hen1 = fabrica.getHen('bel')
print(hen1.getDescription())





