#задача 1
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
        print(f'default_name: {Human.default_name}')
        print(f'default_age: {Human.default_age}')

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def earn_money(self, max_money):
        self.__money += max_money
        print(f'На ваш баланс зачислено {max_money} баксов! Ваш баланс:{self.__money}')

    def buy_house(self, house, disc):
        price = house.final_prace(disc)
        if self.__money >= price:
            self.__make_deal(house, price)
            print("У тебя хватает денег на покупку этого прекрасного сарая")
        else:
            print("К сожалению, у тебя не хватит денег ;((( ")

class House:

    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_prace(self, disc):
        final_prace = self._price * (100 - disc) / 100
        print(f'Финальная цена: {final_prace}')
        return final_prace


class SmallHouse(House):
    default_area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)


'''
+Вызовите справочный метод  default_info() для класса Human()
+Создайте объект класса Human
+Выведите справочную информацию о созданном объекте (вызовите метод info()).
+Создайте объект класса SmallHouse
+Попробуйте купить созданный дом, убедитесь в получении предупреждения.
+Поправьте финансовое положение объекта - вызовите метод earn_money()
+Снова попробуйте купить дом
+Посмотрите, как изменилось состояние объекта класса Human
'''

Human.default_info()

Alex = Human('Alex', 50)
Alex.info()

Small_House = SmallHouse(100_000)
Alex.buy_house(Small_House, 10)

Alex.earn_money(100_000)
Alex.buy_house(Small_House, 10)

Alex.info()





