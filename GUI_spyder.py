import Tkinter as tk

def f(x):
    return x

master = tk()
x = Scale(master, from_ = 0, to = 100)
x.pack()
Button(master, text = 'Show', command = f).pack()

mainloop()


