class EngAlphabet():

    __letters_num = 27

    def __private_method(self):
        print('Это приватный метод')

    def public_num(self):
        print(EngAlphabet.__letters_num)


a = EngAlphabet()
#a.public_num()
#a.__private_method()