from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image

root = Tk()
root.title('learn to code ')
root.iconbitmap('D:\Custom-Icon-Design-Mono-Business-2-Coffee.ico')


root.filename = filedialog.askopenfilename(initialdir="D:\shit", title="files", filetypes = ("jpg", "*"))


root.mainloop()