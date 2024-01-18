from abc import ABC, abstractmethod

class Hen(ABC):
    
    def __init__(self, SSSS, N):
        self.SSSS = SSSS
        self.N = N
    
    @abstractmethod
    def getCountOfEggsPerMonth(self):
        pass

    def getDescription(self):
        return 'Я курица!'