import turtle
import math

def drawHouse(t, length):
    for i in range(4):
        t.forward(length)
        t.right(90)
    t.left(45)
    t.forward(length / math.sqrt(2))
    t.right(90)
    t.forward(length / math.sqrt(2))
    t.right(135)
    t.forward(length)

# окно для рисования
windows = turtle.Screen()

# создаем черепашку
pencil = turtle.Turtle('turtle')

# толщина линии
pencil.pensize(2)

# вызываем функцию
drawHouse(pencil, 100)

# закрываем окно
windows.exitonclick()
