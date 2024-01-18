from Hen import Hen
from random import randint

class BelarusianHen(Hen):

    def __init__(self, SSSS, N):
        self.SSSS = SSSS
        self.N = N
    
    def getCountOfEggsPerMonth(self):
        return self.N

    def getDescription(self):
        return f"{Hen.getDescription(self)} Моя страна- {self.SSSS}. Я несу {self.N} яиц в месяц"

info = BelarusianHen('Belarus', randint(0, 100))
print(info.getDescription())