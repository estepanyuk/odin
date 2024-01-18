import random
import tkinter as tk

def randomizer():
    lbl_randomizer['text'] = str(random.randint(1,6))

windows = tk.Tk()
windows.columnconfigure(0, minsize=150)
windows.rowconfigure([0, 1], minsize=50)

btn_randomizer = tk.Button(text='Бросить', command=randomizer)
lbl_randomizer = tk.Label()

btn_randomizer.grid(row=0, column=0, sticky='nsew')
lbl_randomizer.grid(row=1, column=0)

windows.mainloop()