from tkinter import *
import backbone

def get_selected_member(event):
    try:
        global selected_tuple
        index=t1.curselection()[0]
        selected_tuple= t1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass

def show_command():
    t1.delete(0, END) 
    for element in backbone.show():
        t1.insert(END, element)

def search_command():
    t1.delete(0, END)
    for element in backbone.search(e1_Name.get(), e2_Age.get(), e3_DOB.get(), e4_NickName.get()):
        t1.insert(END, element)

def add_command():
    backbone.add(e1_Name.get(), e2_Age.get(), e3_DOB.get(), e4_NickName.get())
    t1.delete(0, END)
    t1.insert(END, (e1_Name.get(), e2_Age.get(), e3_DOB.get(), e4_NickName.get()))

def delete_command():
    backbone.delete(selected_tuple[0])

def update_command():
    backbone.update(selected_tuple[0], e1_Name.get(), e2_Age.get(), e3_DOB.get(), e4_NickName.get())


window=Tk()

window.wm_title("FamilyBot")

l1= Label(window, text="Name")
l1.grid(row=0, column=0)

l2= Label(window, text="Age")
l2.grid(row=0, column=2)

l3= Label(window, text="DOB")
l3.grid(row=1, column=0)

l4= Label(window, text="NickName")
l4.grid(row=1, column=2)

e1_Name= StringVar()
e1= Entry(window, textvariable=e1_Name)
e1.grid(row=0, column=1)

e2_Age= StringVar()
e2= Entry(window, textvariable=e2_Age)
e2.grid(row=0, column=4)

e3_DOB= StringVar()
e3= Entry(window, textvariable=e3_DOB)
e3.grid(row=1, column=1)

e4_NickName= StringVar()
e4= Entry(window, textvariable=e4_NickName)
e4.grid(row=1, column=4)

t1= Listbox(window, height=6, width=35)
t1.grid(row=2, column=0, rowspan=7, columnspan=2)

sb1= Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

t1.configure(yscrollcommand=sb1.set)
sb1.configure(command=t1.yview)

t1.bind('<<ListboxSelect>>', get_selected_member)

b1= Button(window, text="Show all", width=20, command= show_command)
b1.grid(row=2, column=4)

b2= Button(window, text='Search', width=20, command= search_command)
b2.grid(row=3, column=4)

b3= Button(window, text='Add Member', width=20, command= add_command)
b3.grid(row=4, column=4)

b4= Button(window, text='Update', width=20, command= update_command)
b4.grid(row=5, column=4)

b5= Button(window, text='Delete', width=20, command= delete_command)
b5.grid(row=6, column=4)

b6= Button(window, text='Close', width=20, command=window.destroy)
b6.grid(row=7, column=4)

window.mainloop()