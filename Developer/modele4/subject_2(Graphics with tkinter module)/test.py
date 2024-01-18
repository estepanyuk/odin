
"""
задача 1
Ниже представлен вариант кода для выполнения данного задания.
В следующем варианте для установки фона и цвета шрифта текстового виджета, используются параметры bg и fg.
Помните, что ваша программа может отличаться от нашей, у каждого разработчика свой стиль программирования.
вариант 1
"""

import tkinter as tk

window = tk.Tk()

entry = tk.Entry(width=40, bg="white", fg="black")
entry.pack()

entry.insert(0, "What is your name?")

window.mainloop()

"""
Это хорошее решение, цвет фона и цвет шрифта для виджета однострочного текстового поля Entry указываются довольно просто.

В большинстве систем по умолчанию цвет фона для виджета Entry — белый, а цвет содержимого — черный. Таким образом, вы можете создать то же самое окно, не уточняя при этом параметры bg и fg:
вариант 2
"""
import tkinter as tk

window = tk.Tk()

entry = tk.Entry(width=40)
entry.pack()

entry.insert(0, "What is your name?")

window.mainloop()

#задача 2
import tkinter as tk

window = tk.Tk()

for i in range(3):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)

    for j in range(0, 3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)

        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack(padx=5, pady=5)

window.mainloop()

#задача 3

import random
import tkinter as tk


def roll():
    lbl_result["text"] = str(random.randint(1, 6))


window = tk.Tk()
window.columnconfigure(0, minsize=150)
window.rowconfigure([0, 1], minsize=50)

btn_roll = tk.Button(text="Бросить", command=roll)
lbl_result = tk.Label()

btn_roll.grid(row=0, column=0, sticky="nsew")
lbl_result.grid(row=1, column=0)

window.mainloop()
'''

'''
# задача 4
from tkinter import *

tk = Tk()
c = Canvas(tk, width=640, height=640, bg='white')
c.pack()

# сохраняем номер соданной фигуры в переменную
my_favorite_oval = c.create_oval(0, 0, 50, 50, fill='blue')

def moveBall():
    # передвигаем наш овал на 10 пикселей по обеим осям
    c.move(my_favorite_oval, 10, 10)
    # повторяем через 100 мс (1 секунда)
    c.after(100, moveBall)

# спустя 1 секунду (100 мс) после запуска выполнить moveBall
c.after(100, moveBall)

mainloop()


#задача 6
# подключаем графическую библиотеку
from tkinter import *
# подключаем модули, которые отвечают за время и случайные числа
import time
import random
# создаём новый объект — окно с игровым полем. В нашем случае переменная окна называется tk, и мы его сделали из класса Tk() — он есть в графической библиотеке
tk = Tk()
# делаем заголовок окна — Games с помощью свойства объекта title
tk.title('Game')
# запрещаем менять размеры окна, для этого используем свойство resizable
tk.resizable(0, 0)
# помещаем наше игровое окно выше остальных окон на компьютере, чтобы другие окна не могли его заслонить. Попробуйте 🙂
tk.wm_attributes('-topmost', 1)
# создаём новый холст — 400 на 500 пикселей, где и будем рисовать игру
canvas = Canvas(tk, width=500, height=400, highlightthickness=0)
# говорим холсту, что у каждого видимого элемента будут свои отдельные координаты
canvas.pack()
# обновляем окно с холстом
tk.update()
# Описываем класс Ball, который будет отвечать за шарик
class Ball:
    # конструктор — он вызывается в момент создания нового объекта на основе этого класса
    def __init__(self, canvas, paddle, score, color):
        # задаём параметры объекта, которые нам передают в скобках в момент создания
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        # цвет нужен был для того, чтобы мы им закрасили весь шарик
        # здесь появляется новое свойство id, в котором хранится внутреннее название шарика
        # а ещё командой create_oval мы создаём круг радиусом 15 пикселей и закрашиваем нужным цветом
        self.id = canvas.create_oval(10,10, 25, 25, fill=color)
        # помещаем шарик в точку с координатами 245,100
        self.canvas.move(self.id, 245, 100)
        # задаём список возможных направлений для старта
        starts = [-2, -1, 1, 2]
        # перемешиваем его
        random.shuffle(starts)
        # выбираем первый из перемешанного — это будет вектор движения шарика
        self.x = starts[0]
        # в самом начале он всегда падает вниз, поэтому уменьшаем значение по оси y
        self.y = -2
        # шарик узнаёт свою высоту и ширину
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        # свойство, которое отвечает за то, достиг шарик дна или нет. Пока не достиг, значение будет False
        self.hit_bottom = False
    # обрабатываем касание платформы, для этого получаем 4 координаты шарика в переменной pos (левая верхняя и правая нижняя точки)
    def hit_paddle(self, pos):
        # получаем кординаты платформы через объект paddle (платформа)
        paddle_pos = self.canvas.coords(self.paddle.id)
        # если координаты касания совпадают с координатами платформы
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                # увеличиваем счёт (обработчик этого события будет описан ниже)
                self.score.hit()
                # возвращаем метку о том, что мы успешно коснулись
                return True
        # возвращаем False — касания не было
        return False
    # метод, который отвечает за движение шарика
    def draw(self):
        # передвигаем шарик на заданный вектор x и y
        self.canvas.move(self.id, self.x, self.y)
        # запоминаем новые координаты шарика
        pos = self.canvas.coords(self.id)
        # если шарик падает сверху
        if pos[1] <= 0:
            # задаём падение на следующем шаге = 2
            self.y = 2
        # если шарик правым нижним углом коснулся дна
        if pos[3] >= self.canvas_height:
            # помечаем это в отдельной переменной
            self.hit_bottom = True
            # выводим сообщение и количество очков
            canvas.create_text(250, 120, text='Вы проиграли', font=('Courier', 30), fill='red')
        # если было касание платформы
        if self.hit_paddle(pos) == True:
            # отправляем шарик наверх
            self.y = -2
        # если коснулись левой стенки
        if pos[0] <= 0:
            # движемся вправо
            self.x = 2
        # если коснулись правой стенки
        if pos[2] >= self.canvas_width:
            # движемся влево
            self.x = -2
#  Описываем класс Paddle, который отвечает за платформы
class Paddle:
    # конструктор
    def __init__(self, canvas, color):
        # canvas означает, что платформа будет нарисована на нашем изначальном холсте
        self.canvas = canvas
        # создаём прямоугольную платформу 10 на 100 пикселей, закрашиваем выбранным цветом и получаем её внутреннее имя
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        # задаём список возможных стартовых положений платформы
        start_1 = [40, 60, 90, 120, 150, 180, 200]
        # перемешиваем их
        random.shuffle(start_1)
        # выбираем первое из перемешанных
        self.starting_point_x = start_1[0]
        # перемещаем платформу в стартовое положение
        self.canvas.move(self.id, self.starting_point_x, 300)
        # пока платформа никуда не движется, поэтому изменений по оси х нет
        self.x = 0
        # платформа узнаёт свою ширину
        self.canvas_width = self.canvas.winfo_width()
        # задаём обработчик нажатий
        # если нажата стрелка вправо — выполняется метод turn_right()
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        # если стрелка влево — turn_left()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        # пока платформа не двигается, поэтому ждём
        self.started = False
        # как только игрок нажмёт Enter — всё стартует
        self.canvas.bind_all('<KeyPress-Return>', self.start_game)
    # движемся вправо
    def turn_right(self, event):
        # будем смещаться правее на 2 пикселя по оси х
        self.x = 2
    # движемся влево
    def turn_left(self, event):
        # будем смещаться левее на 2 пикселя по оси х
        self.x = -2
    # игра начинается
    def start_game(self, event):
        # меняем значение переменной, которая отвечает за старт движения платформы
        self.started = True
    # метод, который отвечает за движение платформы
    def draw(self):
        # сдвигаем нашу платформу на заданное количество пикселей
        self.canvas.move(self.id, self.x, 0)
        # получаем координаты холста
        pos = self.canvas.coords(self.id)
        # если мы упёрлись в левую границу
        if pos[0] <= 0:
            # останавливаемся
            self.x = 0
        # если упёрлись в правую границу
        elif pos[2] >= self.canvas_width:
            # останавливаемся
            self.x = 0
#  Описываем класс Score, который отвечает за отображение счетов
class Score:
    # конструктор
    def __init__(self, canvas, color):
        # в самом начале счёт равен нулю
        self.score = 0
        # будем использовать наш холст
        self.canvas = canvas
        # создаём надпись, которая показывает текущий счёт, делаем его нужно цвета и запоминаем внутреннее имя этой надписи
        self.id = canvas.create_text(450, 10, text=self.score, font=('Courier', 15), fill=color)
    # обрабатываем касание платформы
    def hit(self):
        # увеличиваем счёт на единицу
        self.score += 1
        # пишем новое значение счёта
        self.canvas.itemconfig(self.id, text=self.score)
# создаём объект — зелёный счёт
score = Score(canvas, 'green')
# создаём объект — белую платформу
paddle = Paddle(canvas, 'White')
# создаём объект — красный шарик
ball = Ball(canvas, paddle, score, 'red')
# пока шарик не коснулся дна
while not ball.hit_bottom:
    # если игра началась и платформа может двигаться
    if paddle.started == True:
        # двигаем шарик
        ball.draw()
        # двигаем платформу
        paddle.draw()
    # обновляем наше игровое поле, чтобы всё, что нужно, закончило рисоваться
    tk.update_idletasks()
    # обновляем игровое поле и смотрим за тем, чтобы всё, что должно было быть сделано — было сделано
    tk.update()
    # замираем на одну сотую секунды, чтобы движение элементов выглядело плавно
    time.sleep(0.01)
# если программа дошла досюда, значит, шарик коснулся дна. Ждём 3 секунды, пока игрок прочитает финальную надпись, и завершаем игру
time.sleep(3)

# задача 6
from tkinter import *

def output(event):
    # получаем содержимое текстового поля
    s = ent.get()
    try:
        txt = open(s, "r", encoding="utf-8")
        content = txt.read()
        tex.delete(1.0, END)
        tex.insert(END, content)
    except:
        tex.delete(1.0, END)
        tex.insert(END, "Файл не существует!")


root = Tk()
root.title("Просмотрщик файлов")
root.minsize(width=500, height=400)

# создаем виджеты
ent = Entry(root, width=20)
but = Button(root, text="Открыть")
tex = Text(root, width=80, height=30, font="Courier 14", wrap=WORD)
tex.insert(END, "Введите имя текстового файла и нажмите кнопку Открыть")

# распологаем виджеты в окне программы
ent.grid(row=0, column=0)
but.grid(row=2, column=0)
tex.grid(row=1, column=0)

# устанавливаем обработчик событий
but.bind("<Button-1>", output)

# запускаем программу
root.mainloop()


