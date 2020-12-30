from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('learn to code ')
root.iconbitmap('D:\Custom-Icon-Design-Mono-Business-2-Coffee.ico')

r = IntVar()
r.set("2")


def click(value):
    myLabel= Label(root, text =value)
    myLabel.pack()


Radiobutton(root, text = "option 1",variable= r, value =1, command = lambda :click(r.get).pack()
Radiobutton(root, text = "option 2",variable= r, value =2,command = lambda : click(r.get)).pack()


myLabel = Label(root, text= r.get())
myLabel.pack()

root.mainloop()