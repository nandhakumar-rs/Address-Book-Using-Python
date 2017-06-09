from tkinter import *
from database import Database

storage = Database()


class Application():
    def __init__(self, window):

        def get_selected(event):
            global tuple
            index = lst.curselection()
            tuple = lst.get(index)
            entry1.delete(0, END)
            entry1.insert(END, tuple[1])
            entry2.delete(0, END)
            entry2.insert(END, tuple[2])
            entry3.delete(0, END)
            entry3.insert(END, tuple[3])
            entry4.delete(0, END)
            entry4.insert(END, tuple[4])
            entry5.delete(0, END)
            entry5.insert(END, tuple[5])

        def select_view():
            lst.delete(0, END)
            for data in storage.view():
                lst.insert(END, data)

        def view_all():
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)

            lst.delete(0, END)
            for data in storage.view():
                for item in data:
                    lst.insert(END, item)
                lst.insert(END, "-------------")

        def insert_data():
            storage.insert(e1.get(), e2.get(), e3.get(), e4.get(), e5.get())
            lst.delete(0, END)
            lst.insert(END, "Your Address has been Added.....:)")

        def search_data():
            lst.delete(0, END)
            for data in storage.search(e1.get(), e2.get(), e3.get(), e4.get(), e5.get()):
                for item in data:
                    lst.insert(END, item)
                lst.insert(END, "-------------")

        def delete_data():
            storage.delete(tuple[0])

        def update_data():
            storage.update(e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), tuple[0])

        def close_window():
            exit(0)

        window.wm_title("Address Book")
        window.wm_iconbitmap("contact.ico")
        lable1 = Label(window, text="Name")
        lable1.grid(row=0, column=0)
        lable2 = Label(window, text="E-Mail")
        lable2.grid(row=1, column=0)
        lable3 = Label(window, text="Mobile")
        lable3.grid(row=2, column=0)
        lable4 = Label(window, text="City")
        lable4.grid(row=3, column=0)
        lable5 = Label(window, text="Pincode")
        lable5.grid(row=4, column=0)
        e1 = StringVar()
        entry1 = Entry(window, textvariable=e1)
        entry1.grid(row=0, column=1)
        e2 = StringVar()
        entry2 = Entry(window, textvariable=e2)
        entry2.grid(row=1, column=1)
        e3 = StringVar()
        entry3 = Entry(window, textvariable=e3)
        entry3.grid(row=2, column=1)
        e4 = StringVar()
        entry4 = Entry(window, textvariable=e4)
        entry4.grid(row=3, column=1)
        e5 = StringVar()
        entry5 = Entry(window, textvariable=e5)
        entry5.grid(row=4, column=1)
        addbtn = Button(window, text="Add Address", command=insert_data)
        addbtn.grid(row=5, column=0, columnspan=2)
        lst = Listbox(window, height=8, width=30)
        lst.grid(row=0, column=2, rowspan=5)
        lst.bind('<<ListboxSelect>>', get_selected)
        scroll = Scrollbar(window)
        scroll.grid(row=0, column=3, rowspan=6)
        lst.configure(yscrollcommand=scroll.set)
        scroll.configure(command=lst.yview)
        btn1 = Button(window, text="View All", width=15, command=view_all)
        btn1.grid(row=0, column=4)
        btn2 = Button(window, text="Search", width=15, command=search_data)
        btn2.grid(row=1, column=4)
        btn3 = Button(window, text="Update", width=15, command=update_data)
        btn3.grid(row=2, column=4)
        btn4 = Button(window, text="Select", width=15, command=select_view)
        btn4.grid(row=3, column=4)
        btn4 = Button(window, text="Delete", width=15, command=delete_data)
        btn4.grid(row=4, column=4)
        btn5 = Button(window, text="Close", width=15, command=window.destroy)
        btn5.grid(row=5, column=4)


window = Tk()
Application(window)
window.mainloop()
