from tkinter import *

windows = Tk()
oval = Canvas(windows, width=640, height=640, bg='white')
oval.pack()

start_coordinates = oval.create_oval(0, 0, 50, 50, fill='purple')

def moveOval():
    oval.move(start_coordinates, 10, 10)
    oval.after(100, moveOval)

oval.after(100, moveOval())

mainloop()