from tkinter import *

import BackEnd
from BackEnd import view, insert, search, delete, update

def view_all():
    LB.delete(0, END)
    for v in view():
        LB.insert(END, v)

def Search():
    LB.delete(0, END)
    sc = search(title_value.get(), author_value.get(), rating_value.get(), ISBN_value.get())
    for s in sc:
        LB.insert(END, s)

def add():
    new_entry = (title_value.get(), author_value.get(), rating_value.get(), ISBN_value.get())
    LB.delete(0, END)
    insert(title_value.get(), author_value.get(), rating_value.get(), ISBN_value.get())
    LB.insert(END, 'The following record has been successfully added:')
    LB.insert(END, new_entry)

def get_selected_row(event):  # for a function bound with an event, the parameter, event, has to be inside bracket
    global selected_row  # to use selected_row outside of the function, declare it to be a global variable
    index = LB.curselection()[0]  # (listbox object).curselection() returns the index of a selected item
    selected_row = LB.get(index)  # (listbox object).get(x) returns the entire row in tuple whose index is x
    print(selected_row)
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry1.insert(END, selected_row[1])
    entry2.insert(END, selected_row[2])
    entry3.insert(END, selected_row[3])
    entry4.insert(END, selected_row[4])

def Delete():
    LB.delete(0, END)
    delete(selected_row[0])
    LB.insert(END, 'The following record has been deleted:')
    LB.insert(END, selected_row[1:])

def Update():
    entry_updated = (title_value.get(), author_value.get(), rating_value.get(), ISBN_value.get())
    LB.delete(0, END)
    update(selected_row[0], title_value.get(), author_value.get(), rating_value.get(), ISBN_value.get())
    LB.insert(END, 'The original entry:')
    LB.insert(END, (selected_row[1], selected_row[2], selected_row[3], selected_row[4]))
    LB.insert(END, 'has been updated to:')
    LB.insert(END, entry_updated)

window = Tk()
window.title('BookSearchEngine')

lbl1 = Label(window, text = 'Title', width = 10)
lbl1.grid(row=0, column=0)

title_value = StringVar()
entry1 = Entry(window, textvariable = title_value, width = 30)
entry1.grid(row=0, column=1)

lbl2 = Label(window, text = 'Author', width = 10)
lbl2.grid(row=0, column=3)

author_value = StringVar()
entry2 = Entry(window, textvariable = author_value, width = 30)
entry2.grid(row=0, column=4)

lbl3 = Label(window, text = 'Rating', width = 10)
lbl3.grid(row=1, column=0)

rating_value = StringVar()
entry3 = Entry(window, textvariable = rating_value, width = 30)
entry3.grid(row=1, column=1)

lbl4 = Label(window, text = 'ISBN', width = 10)
lbl4.grid(row=1, column=3)

ISBN_value = StringVar()
entry4 = Entry(window, textvariable = ISBN_value, width = 30)
entry4.grid(row=1, column=4)

LB = Listbox(window, height = 12, width = 50)
LB.grid(row=3, column=0, rowspan=4, columnspan=4)

scroll_ybar = Scrollbar(window, width = 20)
scroll_ybar.grid(row=3, column=4, rowspan=4, sticky=N+S+W) # use sticky=N+S+W to make scroll_bar strech towards north, south and west

scroll_xbar = Scrollbar(window, width = 20, orient = 'horizontal')
scroll_xbar.grid(row=2, column=0, columnspan=4, sticky=W+E+S)

#connnect scrollbar and text together
LB.configure(xscrollcommand = scroll_xbar.set, yscrollcommand = scroll_ybar.set)
scroll_xbar.configure(command = LB.xview) # when the scroll bar is scrolled, x-view of listbox is changed.
scroll_ybar.configure(command = LB.yview) # when the scroll bar is scrolled, y-view of listbox is changed.

LB.bind('<<ListboxSelect>>', get_selected_row) # bind event and function together: once the event occurs, the function is run.

all_b = Button(window, text = 'View all', height = 2, width = 20, command = view_all)
all_b.grid(row=2, column=4)

search_b = Button(window, text = 'Search entry', height = 2, width = 20, command = Search)
search_b.grid(row=3, column=4)

add_b = Button(window, text = 'Add entry', height = 2, width = 20, command = add)
add_b.grid(row=4, column=4)

update_b = Button(window, text = 'Update', height = 2, width = 20, command = Update)
update_b.grid(row=5, column=4)

delete_b = Button(window, text = 'Delete', height = 2, width = 20, command = Delete)
delete_b.grid(row=6, column=4)

close_b = Button(window, text = 'Close', height = 2, width = 20, command = window.destroy)  # use window.destroy to close the application
close_b.grid(row=7, column=4)

window.mainloop()
