from tkinter import *

def output():
    #получение содержимого текстового поля
    a = ent.get()

    try:
        tekst = open(a, 'r', encoding='utf8')
        read = tekst.read()
        tekst.delete(1.0, END)
        tekst.insert(END, read)
    except:
        tekst.delete(1.0, END)
        tekst.insert(END, 'Файл не существует')

windows = Tk()
windows.title('')
windows.minsize(width=, height=)

#создаете виджеты
ent = Entry(windows, width=)