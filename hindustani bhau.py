from tkinter import *
from PIL import ImageTk,Image
from tkinter import  messagebox

root = Tk()
root.title('learn to code ')
root.iconbitmap('D:\Custom-Icon-Design-Mono-Business-2-Coffee.ico')

my_image = ImageTk.PhotoImage(Image.open("D:\hb.jpg"))
my_label = Label(image=my_image)
my_label.pack()


def popup():
    response = messagebox.askyesno("Hindustani bhau's message ", "pehli fursat me nikal")
    if response == 1:
        Label(root, text =" subah ke pehli ticket kaat aur nikal").pack()
    else:
        Label(root,text= "jadugar hai tu ya teri maa gayi thi jadugar ke pass").pack()


Button(root, text= "ek baap ke aulad hai to click kar", command = popup).pack()

root.mainloop()