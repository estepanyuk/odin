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

class EngAlphabet(Alphabet):

    __letters_num = 27

    def __init__(self):
        super().__init__('Eg', string.ascii_uppercase)

    #проверка, относится ли буква к английскому алфавиту
    def is_in_letter(self, letters):
        if letters.upper() in self.letters:
            return True
        return False

    #возвращает количество букв в алфавите
    def letters_num(self):
        return EngAlphabet.__letters_num

    @staticmethod
    def example():
        print('qwerty')


if __name__ == '__main__':
    #Создали объект класса EngAlphabet()
    obj = EngAlphabet()
    obj.print()
    print(obj.letters_num())
    print(obj.is_in_letter('F'))
    print(obj.is_in_letter('г'))
    EngAlphabet.example()










