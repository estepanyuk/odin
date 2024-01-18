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

        # label = tk.Label(master=frame, text=f'Row{i}\n Column{j}')
        # label.pack()

        btn = tk.Button(master=frame, text=f'Row{i}\n Column{j}')
        btn.pack()

windows.mainloop()
