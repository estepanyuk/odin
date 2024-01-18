class Human:

    #статические поля
    default_name = 'No name'
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        #Динамические поля
        #публичные
        self.name = name
        self.age = age
        #приватные
        self.__money = 0
        self.__house = None


    def info(self):
        print(f'Name:{self.name}')
        print(f'Age:{self.age}')
        print(f'Money:{self.__money}')
        print(f'House:{self.__house}')

    #статический метод
    @staticmethod
    def default_info():
        print(f'default_name: {Human.default_name}')
        print(f'default_age: {Human.default_age}')

    #Приватный метод
    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def earn_money(self, payday):
        self.__money += payday
        print(f'Заработали: {payday}, денег, {self.__money}')

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(house, price)
        else:
            print('не достаточно денег')


class House:

    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        final_price = self._price * (100 - discount) / 100
        print(f'final_price: {final_price}')
        return final_price

class SmallHouse(House):

    default_area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)


Human.default_info()

Ivan = Human('Ivan', 19)
Ivan.info()

small_house = SmallHouse(8_500)
Ivan.buy_house(small_house, 5)

Ivan.earn_money(100_000)
Ivan.buy_house(small_house, 5)

Ivan.earn_money(20_000)
Ivan.buy_house(small_house, 5)

Ivan.info()

