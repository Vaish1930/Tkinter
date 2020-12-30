from tkinter import *

from PIL import ImageTk,Image

root = Tk()
root.title('learn to code ')
root.iconbitmap('D:\Custom-Icon-Design-Mono-Business-2-Coffee.ico')
root.geometry("400x400")

clicked = StringVar()
clicked.set("monday")

drop = OptionMenu(root, clicked, "monday","tuesday","wedneday")
drop.pack()

mainloop()