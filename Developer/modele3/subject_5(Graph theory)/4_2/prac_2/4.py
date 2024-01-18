# class Soda:
#     def __init__(self, ingredient=None):
#         self.ingredient = ingredient
#
#     def show_my_drink(self):
#         if self.ingredient:
#             print(f'Газировка и {self.ingredient}')
#         else:
#             print('Обычная газировка')

class Soda:
    def __init__(self, dobavka=None):
        self.dobavka = dobavka
    def show_my_drink(self):
        if not self.dobavka:
            print("Обычная газировка")
        else:
            print(f"В газировке есть {self.dobavka}")

drink = Soda()
drink1 = Soda('Малина')
drink2 = Soda(10)
drink.show_my_drink()
drink1.show_my_drink()
drink2.show_my_drink()