import random
from tkinter import *
import time

#окно с игровым полем
windows = Tk()

# заголовок окна
windows.title('Game')

# запрет на смену размера окна
windows.resizable(0, 0)

# наше игровое поле будет на переднем плане на компьютере
windows.wm_attributes('-topmost', 1)

# создали наш холст
canvas = Canvas(windows, width=500, height=400, highlightthickness=0)
canvas.pack()
windows.update()

class Ball:
    def __init__(self, canvas, paddle, score, color):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.id = canvas.create_oval(10,10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-2, -1, 1, 2]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -2
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    # обработка касания нашей платформы
    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                self.score.hit()
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        # падает сверху
        if pos[1] <= 0:
            self.y = 2
        # если правый нижним углом коснулся дна
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            canvas.create_text(250, 120, text='Вы проиграли', font=('Courier', 30), fill='red')
        if self.hit_paddle(pos) == True:
            self.y = -2
        if pos[0] <= 0:
            self.x = 2
        if pos[2] >= self.canvas_width:
            self.x = -2

# описываем класс Paddle, который отвечает за платформу
class Paddle:
    # конструктор
    def __init__(self, canvas, color):
        # рисуем платформу
        self.canvas = canvas
        # создаем прямоугольную платформу 10 на 100 пикселей
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        # список возможных стартовых положений платформы
        start_1 = [40, 60, 90, 120, 150, 180, 200]
        # перемешиваем
        random.shuffle(start_1)
        # выбираем первое перемещение
        self.starting_point_x = start_1[0]
        self.canvas.move(self.id, self.starting_point_x, 300)
        self.x = 0
        #платформа узнает свою ширину
        self.canvas_width = self.canvas.winfo_width()
        # задаем обработчки событий
        # если нажата стрелка вправа, то у нас выполняется наш метод turn_right()
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        # если нажата стрелка влево, то у нас выполняется наш метод turn_left()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        # платформа не двигается
        self.started = False
        self.canvas.bind_all('<KeyPress-Return>', self.start_game)

    # создание события клавиш
    # смещение вправо на 2 пикселя по оси x
    def turn_right(self, event):
        self.x = 2
    # смещение влево на 2 пикселя по оси x
    def turn_left(self, event):
        self.x = -2

    # начали игру
    def start_game(self, event):
        self.started = True

    # отвечает за движенеи платформы
    def draw(self):
        # двигаем нашу платформу
        self.canvas.move(self.id, self.x, 0)
        # получаем координаты холста
        pos = self.canvas.coords(self.id)
        # если уперлась в левую границу
        if pos[0] <= 0:
            # останавливаемся
            self.x = 0
        # если уперлась в правую границу
        elif pos[2] >= self.canvas_width:
            # останавливаемся
            self.x = 0

class Score:
    def __init__(self, canvas, color):
        self.score = 0
        self.canvas = canvas
        self.id = canvas.create_text(450, 10, text=self.score, font=('Courier', 15), fill=color)

    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.id, text=self.score)

# создfем объекты
score = Score(canvas, 'Mediumvioletred')
paddle = Paddle(canvas, 'White')
ball = Ball(canvas, paddle, score, 'red')

while not ball.hit_bottom:
    if paddle.started == True:
        ball.draw()
        paddle.draw()
    windows.update_idletasks()
    windows.update()
    time.sleep(0.01)

time.sleep(3)
























