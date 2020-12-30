from tkinter import *
from tkinter import Toplevel

from PIL import ImageTk,Image

root = Tk()
root.title('learn to code ')
root.iconbitmap('D:\Custom-Icon-Design-Mono-Business-2-Coffee.ico')


def open():
    t = Toplevel()
    t.iconbitmap('D:\Custom-Icon-Design-Mono-Business-2-Coffee.ico')

    end = Button(t, text = "exit", command =t.destroy).pack()


button = Button(root, text= "click", command = lambda : open()).pack()

mainloop()