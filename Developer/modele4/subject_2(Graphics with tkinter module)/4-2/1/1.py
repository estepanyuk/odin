import tkinter as tk

windows = tk.Tk()

entry = tk.Entry(width=40, background='black', foreground='white')
entry.pack()

entry.insert(0, 'Приятно познакомится, Tkinter')

windows.mainloop()



