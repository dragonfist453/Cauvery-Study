from tkinter import *

def f(x,y):
    return x.get()+y.get()

master = Tk()
x = IntVar()
x = Scale(master, from_ = 0, to = 100,length=300,orient=HORIZONTAL)
x.set(20)
x.pack()
y = IntVar()
y = Scale(master, from_ = 0, to = 100, length=300, orient=HORIZONTAL)
y.set(30)
y.pack()
widget = Button(master, text = 'Show', command = f(x,y)).pack()
w = Label(master, text = str(f(x,y)))
w.pack()
master.mainloop()
