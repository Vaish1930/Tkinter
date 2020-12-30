from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('learn to code ')
root.iconbitmap('D:\Custom-Icon-Design-Mono-Business-2-Coffee.ico')

my_image = ImageTk.PhotoImage(Image.open("D:\corona.jpg"))
my_label = Label(image = my_image)
my_label.pack()

button_quit = Button(root, text= "quit", command = root.quit)

button_quit.pack()


root.mainloop()