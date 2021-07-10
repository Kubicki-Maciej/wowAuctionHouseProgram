# other libraries
from tkinter import ttk
from tkinter import *
from tkinter.ttk import Combobox, Style
from tkinter import filedialog
import tkinter as tk
from PIL import ImageTk, Image
import os

#  my files
import read_ah_file_new as raf
import itemsgui
import find_in_folder as fif
import select_file_by_date as sfd
import mathprice
import settings as st
import comparison as comp


# (object_list.list_items) naprawić dodać list_item_class i z tad pobrac list_item_class.price or buyout

root = Tk()
root.geometry("810x480")


def printest(element, element1, element2):
    """function made to test"""
    # button_test = Button(compareWindow, text="printme",command=lambda: printest(compareWindow.list_of_selected_servers))
    # button_test.place(x=50, y=50, )

    print(element, "element1 ")
    print(element1, "element2 ")
    print(element2, "element3 ")


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
    """  # TO DO

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
    select_day()  # tu powinna sie dziac magia wczytania pliku json z uwzglednieniem dobrej daty dodac opcje recznego
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


def place_item_info(name, id, object_list):
    # Tree selection https://pythonguides.com/python-tkinter-treeview/
    item_name = Label(root, text=name)
    item_name.config(font=("Courier", 18))
    item_name.place(x=450, y=35, in_=root)

    # load IMG
    load_img(id)

    # create avg price
    global list_of_items
    list_of_items = [[], [], []]

    average_price = mathprice.average_price(object_list.list_items)
    avg_price = average_price[4]
    average_price_row = ['average price all', mathprice.split_value(avg_price)]
    list_of_items[0] = average_price_row

    """
    item_avg_price_label = Label(root, text="average price:")
    item_avg_price_label.place(x=450, y=90, in_=root)
    item_avg_price = Label(root, text= mathprice.split_value(avg_price[4]))
    item_avg_price.place(x=540, y=90, in_=root)
    """

    # percent avg
    percent_box = Entry(root, width=10)
    percent_box.place(x=650, y=110, in_=root)

    btn_percent = Button(root, text="percent", width=10,
                         command=lambda: take_avg_percent(percent_box.get(), object_list.list_items, list_of_items,
                                                          root))
    btn_percent.place(x=720, y=106, in_=root)

    x_items = Entry(root, width=10)
    x_items.place(x=650, y=140, in_=root)

    btn_x_items = Button(root, text="buy x items", width=10,
                         command=lambda: take_x_items(x_items.get(), object_list.list_items, list_of_items, root))
    btn_x_items.place(x=720, y=136, in_=root)

    # load tree
    load_tree(root, list_of_items)

    # price for all selected ()


def load_img(id):
    canvas = Canvas(root, width=85, height=85)
    canvas.place(x=650, y=35)
    img = ImageTk.PhotoImage(Image.open("data/img/itemsimg/" + str(id) + ".jpg"))
    canvas.create_image(0, 0, anchor=NW, image=img)
    canvas.image = img


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


def close_save():
    #     save function from settings.py
    servers_window.destroy()


def open_window_select_server():
    global servers_window
    servers_window = Tk()
    servers_window.title("Servers")
    servers_window.geometry("600x400")

    close_button = Button(servers_window, text="close and save", command=close_save)
    close_button.place(x=500, y=350, in_=servers_window)


global my_json


def at_start_open_file_from_settings_if_option_is_selected():
    check_option = st.load_settings(1, st.set_file_name)[3]

    # If Ture open newest file from selected in settings default server row 2
    if check_option:
        # selected_server_id load from settings.csv row = 2 int_value witch represent id server
        # selected_server_id return 2 values
        selected_server_id = st.load_settings(1, st.set_file_name)[2]

        natural_number_server_id = int(selected_server_id)

        file_tuple = sfd.newest_file(sfd.get_files_by_id(natural_number_server_id))

        newest_file = file_tuple[1]

        join_path = os.path.join(sfd.make_path(natural_number_server_id), newest_file[3])
        print(join_path)

        root.filename = (join_path)
        my_json = root.filename

        print('Load selected server from settings ' + newest_file[3])

        root.opened_json_object = raf.AhFile(my_json)
        root.opened_json_object.create_dependency()


def open_file_and_add_it_to_list(list_elements):
    filename = filedialog.askopenfilename(initialdir=(os.getcwd() + '\data\Json'), title="Select a File", filetypes=(
        ("json files", "*.json"), ("all files", "*.*")))
    print(filename)
    list_elements.append(filename)


def open_by_take_from_list_json():
    root.filename = filedialog.askopenfilename(initialdir=(os.getcwd() + '\data\Json'), title="Select a File",
                                               filetypes=(
                                                   ("json files", "*.json"), ("all files", "*.*")))
    my_json = root.filename
    print(my_json)
    root.opened_json_object = raf.AhFile(my_json)
    root.opened_json_object.create_dependency()


def open_new_window():
    global sw
    sw = Tk()
    sw.title("Settings")
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
    itemsObjectList = root.opened_json_object.serch_items(
        get_name)  # z wczesniej stworzonego obiektu w funkcji open_json pobieramy
    # pobieramy funkjca serch_items z klasy AhFile z read_ah_file_new

    # # dodajemy metode sortowania inna dla buyout i unit price
    if itemsObjectList.list_item_class[0].price_unit:
        itemsObjectList.list_items.sort(key=raf.sort_by_price)
    else:
        itemsObjectList.list_items.sort(key=raf.sort_by_buyout)

      # sortujemy liste,

    item_name = itemsObjectList.item_name
    items_object = itemsgui.ItemBox(
        itemsObjectList.list_items)  # towrzymy obiekt i dodajemy do niego wczesniej posortowana liste
    items_object.split_list()  # splitujemy ja bysmy mogli latwo zrobic page 1/10 w klasie itembox powinny byc tuple

    id_item_from_serch = items_object.item_list[0]['item']['id']

    take_items(items_object, item_name, 0)
    place_item_info(item_name, id_item_from_serch, itemsObjectList)

    #  tutaj czyszczenie ? ta metoda nie czysci tylko napisuje na dane miejsce na ten moment

    button_forward = Button(root, text=">>", command=lambda: forward(2, items_object.split_list_items, items_object))
    button_forward.place(x=250, y=400, in_=root)

    button_back = Button(root, text="<<", command=back, state=DISABLED)
    button_back.place(x=150, y=400, in_=root)

    status = Label(root, text="Page 1 of " + str(len(items_object.split_list_items)), bd=1, relief=SUNKEN,
                   anchor=E)
    status.place(x=180, y=405, in_=root)


def take_avg_percent(percent_box, itemsObjList, list_to_add_elements_of_tree, place_to_show):
    percent_value = mathprice.avg_percent_items_price(percent_box, itemsObjList)
    values_to_list = ['value ' + percent_box + '%', mathprice.split_value(percent_value[3][-1])]
    print(values_to_list)
    list_to_add_elements_of_tree[1] = values_to_list
    load_tree(place_to_show, list_to_add_elements_of_tree)


def take_x_items(x_items, itemsObjList, list_to_add_elements_of_tree, place_to_show):
    x_items_value = mathprice.take_average_price_first_x_items(itemsObjList, x_items)
    values_to_list = ['money needed', mathprice.split_value(int(x_items_value[4]))]
    print(values_to_list)
    list_to_add_elements_of_tree[2] = values_to_list

    load_tree(place_to_show, list_to_add_elements_of_tree)


def load_tree(place_used, x):
    # Treeview

    tree2 = ttk.Treeview(place_used, height=3, column=("c1", "c2"), show='headings', )

    tree2.column("#1", anchor=tk.CENTER, minwidth=20, width=100)

    tree2.column("#2", anchor=tk.CENTER, minwidth=20, width=100)

    tree2.place(x=425, y=105, in_=place_used)

    for row in x:
        tree2.insert("", tk.END, values=row)


def load_tree_compare(place_used, x, columns):
    # Treeview
    columns_list = []
    for i in range(len(columns)):
        columns_list.append("server " + str(i + 1))

    tree2 = ttk.Treeview(place_used, height=len(x), column=(columns_list), show='headings', )

    for j in range(len(columns) + 1):
        create_hash = "#" + str(j)
        tree2.column(create_hash, anchor=tk.CENTER, minwidth=20, width=100)

    # tree2.column("#1", anchor=tk.CENTER, minwidth=20, width=100)
    #
    # tree2.column("#2", anchor=tk.CENTER, minwidth=20, width=100)

    tree2.place(x=5, y=105, in_=place_used)

    for row in x:
        tree2.insert("", tk.END, values=row)


def make_compare(list_elemnets, space_to_save_object, compareWindow):
    print('tworze elementy to porównania')
    compare_object = comp.Comparison()
    compareWindow.tree_list = []

    for element in list_elemnets:
        if element:
            raf_ah_object = compare_object.create_object_raf(element)
            compare_object.list_of_raf_file.append(raf_ah_object)
            compareWindow.tree_list.append([])

            # average_price = mathprice.average_price(object_list.list_items)
            # avg_price = average_price[4]

    compare_object.create_dependency_of_ahfile()
    compareWindow.compareObject = compare_object
    box_info = Entry(compareWindow, width=15)
    box_info.place(x=10, y=60, )

    btn_get_compare_servers = Button(compareWindow, text="Item to compare",
                                     command=lambda: get_compare(compareWindow.compareObject, box_info,
                                                                 compareWindow))
    btn_get_compare_servers.place(x=120, y=60, )

    # function create list

    return compare_object


def get_compare(objects, box, compareWindow):
    print('porównuje servery z listy')
    all_lists = []
    list_avg = []
    list_100_avg_percnet = []

    objects.compare(box.get())

    avg_p = objects.avg_price()
    avg_p_first_100_items = objects.make_average_price_first_x_items()
    avg_value_percent = objects.make_avg_percent_price(100)
    min_price_items = objects.min_price()

    rows_names = ["avgp", "avg p 100 items", "avg 100%", "min price"]

    all_lists.append(avg_p)
    all_lists.append(avg_p_first_100_items)
    all_lists.append(avg_value_percent)
    all_lists.append(min_price_items)

    all_lists[0].insert(0, rows_names[0])
    all_lists[1].insert(0, rows_names[1])
    all_lists[2].insert(0, rows_names[2])
    all_lists[3].insert(0, rows_names[3])

    box_x_items = Entry(compareWindow, width=15)
    box_x_items.place(x=320, y=60, )

    btn_get_compare_servers = Button(compareWindow, text="x items to take",
                                     command=lambda: update_compare(compareWindow, all_lists, all_lists[0], objects,
                                                                    box_x_items))
    btn_get_compare_servers.place(x=220, y=60, )

    print(all_lists)

    load_tree_compare(compareWindow, all_lists, all_lists[0])


def update_compare(compareWindow, allist, first_element, object, get_info_from_box, ):
    row_name = "avg price per " + str(get_info_from_box.get())

    avg_p_first_100_items = object.make_average_price_first_x_items(get_info_from_box.get())

    temp_list = []
    temp_list.append(row_name)
    for element in avg_p_first_100_items:
        temp_list.append(element)

    allist[1] = temp_list

    load_tree_compare(compareWindow, allist, first_element)


def make_compare(list_elemnets, space_to_save_object, compareWindow):
    print('tworze elementy to porównania')
    compare_object = comp.Comparison()
    compareWindow.tree_list = []

    for element in list_elemnets:
        if element:
            raf_ah_object = compare_object.create_object_raf(element)
            compare_object.list_of_raf_file.append(raf_ah_object)
            compareWindow.tree_list.append([])

            # average_price = mathprice.average_price(object_list.list_items)
            # avg_price = average_price[4]

    compare_object.create_dependency_of_ahfile()
    compareWindow.compareObject = compare_object
    box_info = Entry(compareWindow, width=15)
    box_info.place(x=10, y=60, )

    btn_get_compare_servers = Button(compareWindow, text="Item to compare",
                                     command=lambda: get_compare(compareWindow.compareObject, box_info,
                                                                 compareWindow))
    btn_get_compare_servers.place(x=120, y=60, )


def compare_by_one_sever_by_time(box_info, time, serverWindow, btn_compare):
    statment = 0

    if time == "today":
        print(1)
        statment = 0
    elif time == "7 days":
        print(2)
        statment = 1
    elif time == "1 month":
        print(3)
        statment = 2

    compare_object = comp.Comparison()
    compare_object.make_objects_add_them_to_file(statment, box_info.get())
    if len(compare_object.list_of_raf_file) > 3:
        serverWindow.geometry(str((len(compare_object.list_of_raf_file) + 1.25) * 100) + "x400")
    compare_object.create_dependency_of_ahfile()

    serverWindow.compare_object = compare_object

    print(box_info)
    print(box_info.get())
    print(type(box_info))

    btn_compare.config(text="Search Item", command=lambda: get_compare(serverWindow.compare_object, box_info,
                                                                       serverWindow))


def compare_server_window():
    serverWindow = Tk()
    serverWindow.title("Compare")
    serverWindow.geometry("400x400")
    serverWindow.compare_object = 0

    def callback(selection):
        print(selection)
        return selection

    list_choice = ["today", "7 days", "1 month"]
    clicked = StringVar()
    clicked.set(list_choice[0])

    drop = OptionMenu(serverWindow, clicked, *list_choice)
    drop.place(x=320, y=10)

    box_info = Entry(serverWindow, width=15)
    box_info.place(x=10, y=10, )

    btn_compare = Button(serverWindow, text="Do Compare",
                         command=lambda: compare_by_one_sever_by_time(box_info, clicked.get(), serverWindow,
                                                                      btn_compare))
    btn_compare.place(x=140, y=10, )

    btnexit = Button(serverWindow, text="EXIT", command=serverWindow.destroy)
    btnexit.place(x=360, y=370, )


def compare_window():
    compareWindow = Tk()
    compareWindow.title("Compare")
    compareWindow.geometry("400x400")

    # object in list with Depndacy_of_ah_file
    compareWindow.compareObject = None

    # return from make compare
    compareWindow.list_items = []

    # string list
    compareWindow.list_of_selected_servers = []

    print(compareWindow.list_of_selected_servers)

    # box_info = Entry(compareWindow, width=15)
    # box_info.place(x=145, y=8, )
    # btn_get_compare_servers = Button(compareWindow, text="Item to compare",
    #                                  command=lambda: get_compare(compareWindow.compareObject[0], box_info,
    #                                                              compareWindow.list_items))
    # btn_get_compare_servers.place(x=270, y=8, )

    btn_compare = Button(compareWindow, text="Do Compare",
                         command=lambda: make_compare(compareWindow.list_of_selected_servers,
                                                      compareWindow.compareObject, compareWindow))
    btn_compare.place(x=140, y=10, )

    button_test = Button(compareWindow, text="printme", command=lambda: printest(compareWindow.list_of_selected_servers,
                                                                                 compareWindow.compareObject,
                                                                                 compareWindow.list_items,

                                                                                 ))
    button_test.place(x=10, y=370, )

    btnopenfile = Button(compareWindow, text="SerchFileToCompare",
                         command=lambda: open_file_and_add_it_to_list(compareWindow.list_of_selected_servers))
    btnopenfile.place(x=10, y=10, )

    btnexit = Button(compareWindow, text="EXIT", command=compareWindow.destroy)
    btnexit.place(x=360, y=370, )


# menu
my_menu = Menu(root)
root.config(menu=my_menu)
file_menu = Menu(my_menu)
my_menu.add_cascade(label="Menu", menu=file_menu)

file_menu.add_command(label="select server", command=compare_server_window)
# file_menu.add_separator()
file_menu.add_command(label="compare servers", command=compare_window)
file_menu.add_command(label="quit", command=root.destroy)

# setings menu
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Settings", menu=edit_menu)
edit_menu.add_command(label="Change settings", command=open_new_window)

# create label, button and text box for search


# select_server()
label_search = Label(root, text="Item Name")
label_search.place(x=75, y=7, in_=root)
box_search = Entry(root, width=30)
box_search.place(x=145, y=8, in_=root)

button_search = Button(root, text="Search item", command=search)
button_search.place(x=340, y=5, in_=root)

open_json_btn = Button(root, text="Select file", command=open_by_take_from_list_json)
open_json_btn.place(x=5, y=5, in_=root)

# open_json_btn = Button(root, text="Select file", command=open_window_select_server)
# open_json_btn.place(x=5, y=450, in_=root)

at_start_open_file_from_settings_if_option_is_selected()
mainloop()

# def testing():
#     opened_json_object = raf.AhFile('test_file.json')
#     opened_json_object.create_dependency()
#     x = opened_json_object.serch_items('Anchor Weed')
#     x.list_items.sort(key=raf.sort_by_price)
#     items_object = itemsgui.ItemBox(x.list_items)
#
#     id_item_from_serch = items_object.item_list[0]['item']['id']
#     item_name = x.item_name
#
#
#     return x, item_name, id_item_from_serch
#
