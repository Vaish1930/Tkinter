from tkinter import *
from PIL import ImageTk,Image
from tkinter import  messagebox

root = Tk()
root.title('learn to code ')
root.iconbitmap('D:\Custom-Icon-Design-Mono-Business-2-Coffee.ico')






def popup():
    response = messagebox.askyesno("message ", "hello world")
    if response == 1:
        Label(root, text =" yes").pack()
    else:
        Label(root,text= "no").pack()


Button(root, text= "click me", command = popup).pack()

root.mainloop()