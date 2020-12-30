from tkinter import *

from PIL import ImageTk,Image

root = Tk()
root.title('learn to code ')
root.iconbitmap('D:\Custom-Icon-Design-Mono-Business-2-Coffee.ico')
root.geometry("400x400")

var = IntVar()

c= Checkbutton(root, text= "check ", variable = var)
c.pack()

mainloop()