"""
class Test:
    #a = 'привет'
    pass

obj = Test()
#print(obj.a)
setattr(obj, 'value', 5)
print(obj.value)

"""
"""
переменные класса(animal_type)
class Shark:
    animal_type = 'fish'
    loca = 'ocean'
    followers = 5


new_shark = Shark()
print(new_shark.animal_type)
print(new_shark.loca)
print(new_shark.followers)
"""
#переменные экземпляра класса(self.name)
class Shark:
    #переменные класса
    animal_type = 'fish'
    loca = 'ocean'

    # метод-конструктор с переменными экзепляра name и age
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #метод с переменной экзкмпляра followers
    def set_followers(self, followers):
        print("У этой рыбки"+str(followers)+"подписчиков")


#1 oбъект. Установка переменных экземпляра метода-констурктора
sammy = Shark('Sammy', 15)
print(sammy.name)
print(sammy.age)
print(sammy.animal_type)
print(sammy.loca)
sammy.set_followers(20)


banan = Shark('Banan', 10)
print(banan.name)
print(banan.age)



