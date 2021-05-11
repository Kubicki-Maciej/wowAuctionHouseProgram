from tkinter import *
from read_ah_file import list_multi_class
import read_ah_file_new as raf
from tkinter import filedialog
import itemsgui

root = Tk()
root.geometry("800x600")


# select file button window etc

def open_json():

    root.filename = filedialog.askopenfilename(initialdir="F:/WoWAuctionApi", title="Select a File", filetypes=(
        ("json files", "*.json"),("all files", "*.*")))

    global my_json
    my_json = root.filename
    print(my_json)

    root.opened_json_object = raf.AhFile(my_json)

    root.opened_json_object.create_dependency()



def open_new_window():
    global sw
    sw = Tk()
    sw.title("Update a record")
    sw.geometry("400x400")

def take_items(itemsg, name):
    """represent 8 first items from serch function """

    # z nazwa pobrac ja z object list_item_clas
    print(itemsg.split_list_items)
    itemsg.box_items(root, itemsg.start_box_items(0))



def search():
    # szukanie przez nazwe

    get_name = box_search.get() #pobieramy nazwe z boxa
    x = root.opened_json_object.serch_items(get_name) # z wczesniej stworzonego obiektu w funkcji open_json pobieramy
    #pobieramy funkjca serch_items z klasy AhFile z read_ah_file_new
    x.list_items.sort(key=raf.sort_by_price) # sortujemy liste
    item_name = x.item_name
    items_object = itemsgui.ItemBox(x.list_items) # towrzymy obiekt i dodajemy do niego wczesniej posortowana liste
    items_object.split_list() #splitujemy ja bysmy mogli latwo zrobic page 1/10 w klasie itembox powinny byc tuple

    take_items(items_object, item_name)




"""
def search():
    get_name = box_search.get()
    if get_name in lista:
        print('jest to w liście')
"""

# create label, button and text box for search


label_search = Label(root, text="serch")
label_search.grid(row=1, column=4)
box_search = Entry(root, width=30)
box_search.grid(row=1, column=5)

button_search = Button(root, text="serch item", command=search)
button_search.grid(row=1, column=6)


open_json_btn = Button(root, text="Select server", command=open_json).grid(row=0,column=1)


mainloop()
