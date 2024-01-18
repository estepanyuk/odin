import tkinter as tk

windows = tk.Tk()

for i in range(3):
    windows.columnconfigure(i, weight=1, minsize=75)
    windows.rowconfigure(i, weight=1, minsize=75)

    for j in range(3):
        frame = tk.Frame(
            master=windows,
            relief=tk.RAISED,
            borderwidth=1
        )

        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text=f'Row {i}\n Column{j}')
        label.pack(padx=5, pady=5)

windows.mainloop()

from tkinter import *
from tkinter import ttk

okno = Tk()
okno.title("Хаха, я раньше")
okno.geometry("250x200")

for c in range(3): okno.columnconfigure(index=c, weight=1)
for r in range(3): okno.rowconfigure(index=r, weight=1)

for r in range(3):
    for c in range(3):
        btn = ttk.Button(text=f"({r},{c})")
        btn.grid(row=r, column=c)

okno.mainloop()