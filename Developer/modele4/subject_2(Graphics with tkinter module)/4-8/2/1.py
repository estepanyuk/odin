from tkinter import *
import time
import random

# настройка игрового поля
# создали новый объект-окно с игровым полем
tk = Tk()
tk.title('Game')
tk.resizable(0, 0)
tk.wm_attributes('-topmost', -1)
canvas = Canvas(tk, width=500, height=400)
canvas.pack()
tk.update()

# описываем класс Ball, который будет отвечать за шарик
class Ball:
    # конструктор
    def __init__(self, canvas, paddle, score, color):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-2, -1, 1, 2]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -2
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    # обрабатываем касание платформы
    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        # если координаты касания совпадают с координатами платформы
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                # увеливаем счет
                self.score.hit()
                # успешно коснулись платформы
                return True
        # касание не было
        return False

    #обработка отрисовки шарика
    def draw(self):
        # передвигаем шарик на заданные координаты x и y
        self.canvas.move(self.id, self.x, self.y)
        # запоминаем новые координаты шарика
        pos = self.canvas.coords(self.id)
        # если шарик падает сверху
        if pos[1] <= 0:
        #задаем падение на следующем шаге = 2
            self.y = 2
        # если шарик правым нижним углом коснулся дна
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            canvas.create_text(250, 120, text='Вы проиграли', font=('Arial', 30), fill='red')
        # если было касания платформы
        if self.hit_paddle(pos) == True:
        # отправляем шарик на вверх
            self.y = -2
        # косания левой стенки
        if pos[0] <= 0:
            # движение вправо
            self.x = 2
        # коснулись правой стенки
        if pos[2] >= self.canvas_width:
            # движение влево
            self.x = -2

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        starts_1 = [40, 60, 90, 120, 150, 180, 200]
        random.shuffle(starts_1)
        self.starting_point_x = starts_1[0]
        self.canvas.move(self.id, self.starting_point_x, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        # задаем обработчик нажатий
        # если нажата стрелка вправо - выполняется метод movement_right()
        self.canvas.bind_all('<KeyPress-Right>', self.movement_right)
        # если нажата стрелка влево - выполняется метод movement_left()
        self.canvas.bind_all('<KeyPress-Left>', self.movement_left)
        self.started = False
        # как только игрок жмет Enter - все стартует
        self.canvas.bind_all('<KeyPress-Return>', self.movement_start)

    def movement_right(self, event):
        self.x = 2

    def movement_left(self, event):
        self.x = -2

    def movement_start(self, event):
        self.started = True

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

class Score:
    def __init__(self, canvas, color):
        self.score = 0
        self.canvas = canvas
        self.id = canvas.create_text(450, 10, text=self.score, font=('Arial', 15), fill=color)

    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.id, text=self.score)

score = Score(canvas, 'green')
paddle = Paddle(canvas, 'White')
ball = Ball(canvas, paddle, score,'red')

while not ball.hit_bottom:
    if paddle.started == True:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()

    time.sleep(0.01)
time.sleep(3)






