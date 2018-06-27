"""
A program that stores this book information
Title, Author
Year, ISBN

User can:

View all records
Search an entry
Add entry
Update entry
Delete
Close
"""
from tkinter import *
from backend import Database

database = Database('books.db')


class Window:

    def __init__(self, window):

        self.window = window

        self.window.wm_title('Bookstore')


        l1 = Label(window, text='Title')
        l1.grid(row=0, column=0)

        l2 = Label(window, text='Author')
        l2.grid(row=0, column=2)

        l3 = Label(window, text='Year')
        l3.grid(row=1, column=0)

        l4 = Label(window, text='ISBN')
        l4.grid(row=1, column=2)

        self.title_data = StringVar()
        self.e1 = Entry(window, textvariable=self.title_data)
        self.e1.grid(row=0, column=1)

        self.author_data = StringVar()
        self.e2 = Entry(window, textvariable=self.author_data)
        self.e2.grid(row=0, column=3)

        self.year_data = StringVar()
        self.e3 = Entry(window, textvariable=self.year_data)
        self.e3.grid(row=1, column=1)

        self.isbn_data = StringVar()
        self.e4 = Entry(window, textvariable=self.isbn_data)
        self.e4.grid(row=1, column=3)

        self.lb = Listbox(window, height=6, width=30)
        self.lb.grid(row=2, column=0, rowspan=6, columnspan=2)

        sb = Scrollbar(window)
        sb.grid(row=2, column=2, rowspan=6)

        self.lb.configure(yscrollcommand=sb.set)
        sb.configure(command=self.lb.yview)

        self.lb.bind('<<ListboxSelect>>', self.get_selected_row)

        b1 = Button(window, text="View All", width=12, command=self.view_command)
        b1.grid(row=2, column=3)

        b2 = Button(window, text="Search Entry", width=12, command=self.search_command)
        b2.grid(row=3, column=3)

        b3 = Button(window, text="Add Entry", width=12, command=self.add_command)
        b3.grid(row=4, column=3)

        b4 = Button(window, text="Update Selected", width=12, command=self.update_command)
        b4.grid(row=5, column=3)

        b5 = Button(window, text="Delete Selected", width=12, command=self.delete_command)
        b5.grid(row=6, column=3)

        b6 = Button(window, text="Close", width=12, command=window.destroy)
        b6.grid(row=7, column=3)

    def get_selected_row(self, event):
        try:
            global selected_tuple
            index = self.lb.curselection()[0]
            selected_tuple = self.lb.get(index)
            self.e1.delete(0, END)
            self.e1.insert(END, selected_tuple[1])
            self.e2.delete(0, END)
            self.e2.insert(END, selected_tuple[2])
            self.e3.delete(0, END)
            self.e3.insert(END, selected_tuple[3])
            self.e4.delete(0, END)
            self.e4.insert(END, selected_tuple[4])
        except IndexError:
            pass

    def view_command(self):
        self.lb.delete(0, END)
        for row in database.view():
            self.lb.insert(END, row)

    def search_command(self):
        self.lb.delete(0, END)
        for row in database.search(self.title_data.get(), self.author_data.get(), self.year_data.get(), self.isbn_data.get()):
            self.lb.insert(END, row)

    def add_command(self):
        database.insert(self.title_data.get(), self.author_data.get(), self.year_data.get(), self.isbn_data.get())
        self.lb.delete(0, END)
        self.lb.insert(END, (self.title_data.get(), self.author_data.get(), self.year_data.get(), self.isbn_data.get()))
        self.view_command()

    def update_command(self):
        database.update(selected_tuple[0], self.title_data.get(), self.author_data.get(), self.year_data.get(), self.isbn_data.get())
        self.view_command()
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)
        self.e4.delete(0, END)

    def delete_command(self):
        database.delete(selected_tuple[0])
        self.view_command()


window = Tk()
Window(window)
window.mainloop()
