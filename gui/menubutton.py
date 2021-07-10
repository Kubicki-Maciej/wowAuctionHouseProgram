#https://youtu.be/OPUSBBD2OJw?t=323
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import tkinter as tk

root = Tk()
root.title('test')
root.geometry('400x400')


# img = ImageTk.PhotoImage(Image.open("gui/38.jpg"))
# canvas.create_image(0, 0, anchor=NW, image=img)
def our_command():
    print("hello")
    pass

def selected():
    canvas = Canvas(root, width=85, height=85)
    canvas.place(x=20, y=300)
    img = ImageTk.PhotoImage(Image.open("gui/38.jpg"))
    canvas.create_image(20,20, anchor=NW, image=img)
    # canvas.image = img

    # canvas = Canvas(root, width=300, height=300)
    # canvas.pack()
    # img = PhotoImage(file="gui/38.jpg")
    # canvas.create_image(20, 20, anchor=NW, image=img)

lista = ['pobierz dane','analizuj dane z ostanich 7 dni','wyjdz']
"""
l1 = Label(root,text= "select your server")
l1.grid(row=0,column=0)


cmb = ttk.Combobox(root, value= lista, width= 10)
cmb.grid(row=1,column=0)
cmb.current(0)
"""
clicked = StringVar()
clicked.set(lista[0])

my_menu = Menu(root)
root.config(menu=my_menu)
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="new.." ,command=our_command)
file_menu.add_separator()
file_menu.add_command(label="quit", command=root.destroy)



edit_menu = Menu(my_menu)
my_menu.add_cascade(label= "edit", menu=edit_menu)


btn_percent = Button(root, text="percent", height=1 , width=18)
btn_percent.place(x=100, y=100, in_=root)
drop = OptionMenu(root, clicked, *lista)
drop.pack(pady=20)


myButton = Button(root, text = "select from list", command= lambda:load_tree(tk.CENTER,x))
myButton.pack()


x = ['1','2','3','4']
def load_tree(place_used, list_of_items):
    # Treeview

    tree2 = ttk.Treeview(root, height=3, column=("c1", "c2"), show='headings', )

    tree2.column("#1", anchor=place_used, minwidth=20, width=100)

    tree2.column("#2", anchor=place_used, minwidth=20, width=100)

    tree2.place(x=425, y=105, in_=root)

    for row in list_of_items:
        tree2.insert("", tk.END, values=row)


load_tree(tk.CENTER,x)
root.mainloop()