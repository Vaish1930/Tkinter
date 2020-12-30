from tkinter import *

from PIL import ImageTk,Image

root = Tk()
root.title('learn to code ')
root.iconbitmap('D:\Custom-Icon-Design-Mono-Business-2-Coffee.ico')
root.geometry("400x400")

w = Scale(root, from_=0, to=42, orient=HORIZONTAL)
w.pack()



def slide():
    my = Label(root, text=w.get()).pack()
    root.geometry(str(w.get())+"x400")


my_bt= Button(root, text="click me", command= slide).pack()



mainloop()
