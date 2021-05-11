"""
 tworzymy tutaj tabele z rzeczami z danej profesji
 mozemy dodawać je po nazwie do danej tabeli

"""

import sqlite3
from tkinter import *
import read_ah_file as rah

root = Tk()
root.title("DataBase Menagment")
root.geometry("700x400")

name = "basic.db"



def create_table():
    conn = sqlite3.connect(data_base.get())
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS items (
        id_item integer,
        item_name text,
        picture_url text
    )""")
    conn.commit()
    conn.close()


def add_new_record():
    conn = sqlite3.connect(data_base.get())
    c = conn.cursor()

    id_item = rah.get_from_csv_id_by_name(item_name.get())
    picture_url = "nie ma obrazka bo testy"

    c.execute("INSERT INTO items VALUES (:id_item, :item_name, :picture_url)",
              {
                  'id_item': id_item,
                  'item_name': item_name.get(),
                  'picture_url': picture_url,
              })
    print("dodano do bazy danych "+id_item + " " + item_name.get() + " " + picture_url )
    conn.commit()
    conn.close()


def get_item_info():
    return 1

data_base = Entry(root, width=30)
data_base.grid(row=2, column=2, padx=20, )
data_base_lab = Label(root, text="Name of DB")
data_base_lab.grid(row=2, column=1, padx=20)

item_name = Entry(root, width=30)
item_name.grid(row=3, column=2, )
item_name_label = Label(root, text="Item name")
item_name_label.grid(row=3, column=1, )




# Button Create DB
create_table_button = Button(root, text="create_table_button", command=create_table)
create_table_button.grid(row=2, column=3, columnspan=2, pady=10, padx=10, ipadx=30)

# Button add record to DB
add_rec_btn = Button(root, text="add_rec_btn", command=add_new_record)
add_rec_btn.grid(row=3, column=3, columnspan=2, pady=10, padx=10, ipadx=30)

# Get item info
item_info_button = Button(root, text= "Get item info", command=get_item_info)
item_info_button.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=30)


mainloop()
