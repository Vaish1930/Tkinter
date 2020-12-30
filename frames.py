from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('learn to code ')
root.iconbitmap('D:\Custom-Icon-Design-Mono-Business-2-Coffee.ico')

frame = LabelFrame(root,padx=50,pady=50)
frame.pack(padx=100,pady=100)

b= Button(frame, text="dont click")

b.grid(row= 1, column =0)
b1= Button(frame, text="dont click")
b1.grid(row= 2, column = 2)
root.mainloop()