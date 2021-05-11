#https://youtu.be/OPUSBBD2OJw?t=323
from tkinter import *
from tkinter import ttk

root = Tk()
root.title('test')
root.geometry('400x400')

def selected():
    myLabel = Label(root, text=clicked.get()).pack()

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

drop = OptionMenu(root, clicked, *lista)
drop.pack(pady=20)

myButton = Button(root, text = "select from list", command= selected)
myButton.pack()


root.mainloop()