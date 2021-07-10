from tkinter import StringVar
from tkinter.ttk import Style
from tkinter import *




serverWindow = Tk()

serverWindow.title("Compare")
serverWindow.geometry("400x400")
style = Style(serverWindow)
style.configure("TRadiobutton", background="light green",
                foreground="red", font=("arial", 10, "bold"))
def callback(selection):

    print(clicked.get())


global list_choice
list_choice = ["today", "7 days", "1 month"]
clicked = StringVar()
clicked.set(list_choice[0])

drop = OptionMenu(serverWindow, clicked, *list_choice)
drop.place(x=320, y=80)

box_info = Entry(serverWindow, width=15)
box_info.place(x=10, y=10, )
btn_compare = Button(serverWindow, text="Do Compare",
                     command= lambda:callback(clicked.get()))
btn_compare.place(x=140, y=10, )
btnexit = Button(serverWindow, text="EXIT", command=serverWindow.destroy)
btnexit.place(x=360, y=370, )


mainloop()