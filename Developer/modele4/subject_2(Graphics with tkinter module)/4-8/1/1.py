import tkinter as tk

windows = tk.Tk()

# entry = tk.Entry(width=40, background='white', foreground='black')
entry = tk.Entry(width=40)
entry.pack()

entry.insert(0, 'Привет, очень рад познакомится! Я Tkinter!')

windows.mainloop()
