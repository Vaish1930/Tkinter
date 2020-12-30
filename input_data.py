from tkinter import *

root = Tk()

e = Entry(root, width = 50)
e.pack()
e.get()


def Myclick():
    mylabel = Label(root, text = e.get())
    mylabel.pack()


mybuttons = Button(root, text = "click me", command = Myclick)
mybuttons.pack()

root.mainloop()


