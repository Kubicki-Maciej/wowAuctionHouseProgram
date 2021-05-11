from tkinter import *

master = Tk()
wa = Button(master, text="serch item")
wa.place(x=60,y=30)

w = Canvas(master, width=30, height=30)
w.place(x=0, y=0)
w.create_rectangle(1, 1, 30, 30, fill="red", outline="blue")

master.mainloop()