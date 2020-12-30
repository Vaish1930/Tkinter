from tkinter import *

root = Tk()

def Myclick():
    mylabel = Label(root, text = 'fuck you clicked')
    mylabel.pack()


mybuttons = Button(root, text = "click me", command = Myclick, bg = "blue")
mybuttons.pack()

root.mainloop()


