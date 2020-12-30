from tkinter import *

root = Tk()
root.title("calculator")
e = Entry(root, width = 35, borderwidth = 5)
e.grid(row=0 ,column=0, columnspan = 3, padx = 10, pady=10)


def button_click(number):

    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
     e.insert(0, f_num + int(second_number))

    if math == "subtraction":
     e.insert(0, f_num - int(second_number))

    if math == "multiplication":
     e.insert(0, f_num * int(second_number))

    if math == "division":
     e.insert(0, f_num / int(second_number))


def button_add():
    first_number = e.get()
    global f_num
    global math
    math ="addition"
    f_num = int(first_number)
    e.delete(0, END)


def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)


def button_div():
    first_number = e.get()
    global f_num
    global math
    math = "divison"
    f_num = int(first_number)
    e.delete(0, END)


def button_mul():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)


button1 = Button(root, text= "1", padx=40, pady=20,command= lambda:button_click(1),bg="light yellow")
button2 = Button(root, text= "2", padx=40, pady=20,command= lambda:button_click(2),bg="light yellow")
button3 = Button(root, text= "3", padx=39, pady=20,command= lambda:button_click(3),bg="light yellow")
button4 = Button(root, text= "4", padx=40, pady=20,command= lambda:button_click(4),bg="light yellow")
button5 = Button(root, text= "5", padx=40, pady=20,command= lambda:button_click(5),bg="light yellow")
button6 = Button(root, text= "6", padx=40, pady=20,command= lambda:button_click(6),bg="light yellow")
button7 = Button(root, text= "7", padx=40, pady=20,command= lambda:button_click(7),bg="light yellow")
button8 = Button(root, text= "8", padx=40, pady=20,command= lambda:button_click(8),bg="light yellow")
button9 = Button(root, text= "9", padx=40, pady=20,command= lambda:button_click(9),bg="light yellow")
button0 = Button(root, text= "0", padx=40, pady=20,command= lambda:button_click(0),bg="light yellow")

button_add = Button(root, text= "+", padx=39, pady=20,command= button_add, bg="grey")
button_sub = Button(root, text= "-", padx=41, pady=20,command= button_sub, bg="black", fg="white")
button_mul = Button(root, text= "x", padx=40, pady=20,command= button_mul, bg="grey")
button_div = Button(root, text= "/", padx=40, pady=20,command= button_div, bg="black", fg="white")

button_equal = Button(root, text= "=", padx=91, pady=20,command=button_equal, bg = "light pink")
button_clear = Button(root, text= "clear", padx=79, pady=20,command= button_clear, bg="red",fg="white")

button1.grid(row=3, column=0)
button2.grid(row= 3, column=1)
button3.grid(row=3, column=2)

button4.grid(row= 2, column=0)
button5.grid(row= 2, column=1)
button6.grid(row= 2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)

button_add.grid(row=5, column=0)
button_sub.grid(row=6,column=0)
button_div.grid(row=6,column=1)
button_mul.grid(row=6,column=2)

button_equal.grid(row=5,column=1,columnspan=2)
button_clear.grid(row=4,column=1,columnspan=3)

root.mainloop()
