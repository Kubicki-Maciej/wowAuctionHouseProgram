from tkinter import *
from tkinter.ttk import Combobox
from read_ah_file import list_multi_class
import read_ah_file_new as raf
from tkinter import filedialog
import itemsgui
import find_in_folder as fif


root = Tk()
root.geometry("800x460")


def open_by_select():

    global obj_files
    obj_files = fif.objects_file(fif.load_file(value_server.get()))
    # zrobić funkcje która wybiera najswiezszy po 7 dniach i po 30

# select file button window etc
def selected_server(event):
    """ 
    zrobić łaczenie z realmlist
    jezeli server zostanie wybrany zrobic automatyczne wczytywanie najnowszego servera
    find_in_folder
    """ # TO DO

    file_server = value_server.get()
    print(file_server)
    open_by_select()


def selected_day(event):
    dateselected = value_date.get()

def select_server():
    global value_server
    value_server = StringVar()
    #  wyłaczenie comboboxa 9.05.21
    combobox = Combobox(root, textvariable=value_server)

    combobox.grid(row=0, column=15)
    combobox['values'] = ('1084', 'one week', 'one month')
    combobox.bind("<<ComboboxSelected>>", selected_server)

    #   wyłączenie select_day 9.05.21
    select_day() #tu powinna sie dziac magia wczytania pliku json z uwzglednieniem dobrej daty dodac opcje recznego
    # wybrania pliku ? z listy ? combobox lista o danym id ? z FIF ?


def select_day():
    # wybierasz
    global value_date
    value_date = StringVar()

    combobox = Combobox(root, textvariable=value_date)

    combobox.grid(row=0, column=16)
    combobox['values'] = ('one day', 'one week', 'one month', 'one year')
    combobox.bind("<<ComboboxSelected>>", selected_day)

def forward(number_of_list, len_list, itemsgui_object):
    global button_forward
    global button_back

    take_items(itemsgui_object, "test ", number_of_list - 1)

    button_forward = Button(root, text=">>", command=lambda: forward(number_of_list + 1, len_list, itemsgui_object))
    button_back = Button(root, text="<<", command=lambda: back(number_of_list - 1, len_list, itemsgui_object))

    if number_of_list == len(len_list):
        button_forward = Button(root, text=">>", state=DISABLED)

    button_back.place(x=150, y=400, in_=root)
    button_forward.place(x=250, y=400, in_=root)

    status = Label(root, text=" Page " + str(number_of_list) + " of " + str(len(len_list)), bd=1, relief=SUNKEN,
                   anchor=E)
    status.place(x=180, y=405, in_=root)


def back(number_of_list, len_list, itemsgui_object):
    global button_forward
    global button_back

    take_items(itemsgui_object, "test ", number_of_list - 1)
    button_forward = Button(root, text=">>", command=lambda: forward(number_of_list + 1, len_list, itemsgui_object))
    button_back = Button(root, text="<<", command=lambda: back(number_of_list - 1, len_list, itemsgui_object))

    if number_of_list == 1:
        button_back = Button(root, text="<<", command=back, state=DISABLED)

    button_back.place(x=150, y=400, in_=root)
    button_forward.place(x=250, y=400, in_=root)

    status = Label(root, text=" Page " + str(number_of_list) + " of " + str(len(len_list)), bd=1, relief=SUNKEN,
                   anchor=E)
    status.place(x=180, y=405, in_=root)

def open_by_take_from_list_json():
    root.filename = filedialog.askopenfilename(initialdir="E:/WoWprogram", title="Select a File", filetypes=(
        ("json files", "*.json"), ("all files", "*.*")))

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


def take_items(itemsg, name, number):
    """represent 10 first items from serch function """

    # z nazwa pobrac ja z object list_item_clas

    w = itemsg.split_list_items
    print(itemsg.split_list_items)

    # made function clearing items

    itemsg.box_items(root, itemsg.start_box_items(number))

    return w

def search():
    # szukanie przez nazwe

    get_name = box_search.get()  # pobieramy nazwe z boxa
    x = root.opened_json_object.serch_items(get_name)  # z wczesniej stworzonego obiektu w funkcji open_json pobieramy
    # pobieramy funkjca serch_items z klasy AhFile z read_ah_file_new
    x.list_items.sort(key=raf.sort_by_price)  # sortujemy liste
    item_name = x.item_name
    items_object = itemsgui.ItemBox(x.list_items)  # towrzymy obiekt i dodajemy do niego wczesniej posortowana liste
    items_object.split_list()  # splitujemy ja bysmy mogli latwo zrobic page 1/10 w klasie itembox powinny byc tuple

    take_items(items_object, item_name, 0)


    #  tutaj czyszczenie ? ta metoda nie czysci tylko napisuje na dane miejsce na ten moment




    button_forward = Button(root, text=">>", command=lambda: forward(2, items_object.split_list_items, items_object))
    button_forward.place(x=250, y=400, in_=root)

    button_back = Button(root, text="<<", command=back, state=DISABLED)
    button_back.place(x=150, y=400, in_=root)

    status = Label(root, text="Page 1 of " + str(len(items_object.split_list_items)), bd=1, relief=SUNKEN,
                   anchor=E)
    status.place(x=180, y=405, in_=root)


# create label, button and text box for search

#select_server()
label_search = Label(root, text="Item Name")
label_search.place(x=75, y=7, in_=root)
box_search = Entry(root, width=30)
box_search.place(x=145, y=8, in_=root)

button_search = Button(root, text="Search item", command=search)
button_search.place(x=340, y=5, in_=root)

open_json_btn = Button(root, text="Select file", command=open_by_take_from_list_json)
open_json_btn.place(x=5, y=5, in_=root)

mainloop()
