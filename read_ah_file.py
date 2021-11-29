import realmlist as rl
import item as sin
import items as mul
import csv

"""
 https://www.wowhead.com/item=123865   id=82800 = pet_cage
 test['auctions'][0]['item']['id']
"""

def take_newest_file_by_id(id_file= 1305):
    import select_file_by_date
    files, file = select_file_by_date.newest_file(select_file_by_date.get_files_by_id(id_file))
    return file[4]


f_name = take_newest_file_by_id()


file_open = rl.open_json_file(f_name) #taking name file

list_single_class = []
list_multi_class = [] # list with objects
id_list = []

def sort_by_id(list):
    """
    :param list:
    :return: return json list file sorted by id
    """
    return list['item']['id']


file = file_open['auctions']
file.sort(key=sort_by_id)


def add_to_multi(id_item):
    mutli_object = mul.Items()
    mutli_object.id_items = id_item
    return mutli_object


def add_to_single(row):
    single_object = sin.Item()
    selected_item = file[row]

    single_object.id_item = selected_item['item']['id']
    if 'unit_price' in file[row]:
        single_object.price_unit = file[row]['unit_price']
    elif 'buyout' in file[row]:
            single_object.price_buyout = file[row]['buyout']
    else:
        single_object.price_buyout = file[row]['bid']


    single_object.quantity = selected_item['quantity']
    single_object.time_left = selected_item['time_left']

    single_object.all_data_item = selected_item
    list_single_class.append(single_object)
    return single_object

def get_from_csv_name_by_id(id):
    """ function not used """

    id_item = id
    str_id_item = str(id_item)
    with open('items.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['id'] == str_id_item:
                return row['name item']

def get_from_csv_id_by_name(name):
    name_by = name
    name_ = str(name_by)
    with open('items.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['name item'] == name_:
                return row['id']

def get_info_from_multi_class_by_id(id):
    """ find better algoritm serching
    function return items object
    """
    for item in list_multi_class:
        if item.id_items == id:
            return item




def create_dependency():
    """
    main function that is used to form classes item,items
    taking from json parameters, and scraping website to get name of item
    """

    x = 0
    y = 0
    id = file[x]['item']['id']
    id_list.append(file[x]['item']['id'])

    object_items = add_to_multi(file[x]['item']['id'])
    list_multi_class.append(object_items)
    object_items.start()
    #object_items.item_name = get_from_csv_name_by_id(object_items.id_items) bardzo nie optymalne

    for i in range(len(file)):

        if id == file[y]['item']['id']:
            item = add_to_single(y)
            object_items.list_item_class.append(item)
            object_items.list_items.append(file[y])
            y += 1

        else:
            x = y
            object_items = add_to_multi(file[x]['item']['id'])
            object_items.start()
            #object_items.item_name = get_from_csv_name_by_id(object_items.id_items)
            list_multi_class.append(object_items)
            item = add_to_single(y)
            object_items.list_item_class.append(item)
            object_items.list_items.append(file[y])
            id = file[y]['item']['id']
            id_list.append(file[y]['item']['id'])
            y += 1


create_dependency()
