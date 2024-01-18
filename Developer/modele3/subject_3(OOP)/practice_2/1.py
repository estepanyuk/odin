#задача 1
import string

#алфавит
class Alphabet:

    def __init__(self, language, letters_str):
        self.lang = language
        self.letters = list(letters_str)

    #Печатаем все буквы алфавита
    def print(self):
        print(self.letters)

    #возвращение количетсво букв в алфавите
    def letters_num(self):
        return len(self.letters)

#Английский алфавит
class EngAlphabet(Alphabet):

    __letters_num = 26

    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

    #проверка, относится ли буква к английскому алфавиту
    def is_en_letter(self, letter):
        if letter.upper() in self.letters:
            return True
        return False

    #Возвращаем количество букв в алфавите
    def letters_num(self):
        return EngAlphabet.__letters_num

    #Печатаем пример текста на английском языке
    @staticmethod
    def example():
        print('qwerty')

'''
+Создайте объект класса EngAlphabet
+Напечатайте буквы алфавита для этого объекта
+Выведите количество букв в алфавите
+Проверьте, относится ли буква F к английскому алфавиту
+Проверьте, относится ли буква Щ к английскому алфавиту
Выведите пример текста на английском языке
'''

obj = EngAlphabet()
obj.print()
print(obj.letters_num())
print(obj.is_en_letter('F'))
print(obj.is_en_letter('Щ'))
obj.example()

