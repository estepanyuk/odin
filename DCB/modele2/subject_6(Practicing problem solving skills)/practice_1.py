class Human:

    #Статические поля
    default_name = 'No name'
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        #Динамическме поля
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(f'Имя: {self.name}')
        print(f'Возраст: {self.age}')
        print(f'Деньги: {self.__money}')
        print(f'Дом: {self.__house}')
    @staticmethod
    def default_info():
        print(Human.default_name,Human.default_age)
        print(":_)")


    def __make_deal(self,COSTA,DOMIK):
        self.__money -= COSTA
        self.__house = DOMIK

    def earn_money(self,MAYNER):
        self.__money += MAYNER
        print('ЧУДО!!!! Мама перевала вам на вкусняшки ',MAYNER,'.руб')
        print(f'Теперь на вашем бомжатском балансе {self.__money}')
    #def buy_house(self,house,disceord):
    #    if self.__money