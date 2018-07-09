from tkinter import *

window = Tk()


def convert():
    grams = float(data.get())*1000
    t_low1.delete('1.0', END)
    t_low1.insert(END, grams)
    pounds = float(data.get())*2.20462
    t_low2.delete('1.0', END)
    t_low2.insert(END, pounds)
    ounces = float(data.get())*35.274
    t_low3.delete('1.0', END)
    t_low3.insert(END, ounces)


l1 = Label(window, width=20, height=1, text='Kg')
l1.grid(row=0, column=0)

data = StringVar()
e1 = Entry(window, textvariable=data)
e1.grid(row=0, column=1)

b1 = Button(window, text='Convert', command=convert)
b1.grid(row=0, column=2)

t_low1 = Text(window, width=20, height=1)
t_low1.grid(row=1, column=0)

t_low2 = Text(window, width=20, height=1)
t_low2.grid(row=1, column=1)

t_low3 = Text(window, width=20, height=1)
t_low3.grid(row=1, column=2)


window.mainloop()
