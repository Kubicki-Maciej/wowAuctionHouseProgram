import realmlist as rl
import item as sin
import items as mul
import csv
from csv import writer
import binear_search as bs
import pandas as pd
import time
import csvsort as scv


# tic = time.perf_counter()


def load_choices_items(name):
    """ load csv file and return values """
    data = pd.read_csv(name, sep=',')

    return data.values


def return_key(objectList):
    if ('unit_price') in objectList[0]:
        key = 'unit_price'
    else:
        key = 'buyout'
    return key


def sort_by_id(list):
    """
    :param list:
    :return: return json list file sorted by id
    """
    return list['item']['id']


def check_sort(list):
    if list.list_item_class.price_buyout:
        print('sort_by_buyout(list)')
        return sort_by_buyout(list)

    if list.list_item_class.price_unit:
        print('sort_by_price(list)')
        return sort_by_price(list)


def sort_by_buyout(list):
    return list['buyout']


def sort_by_price(list):
    return list['unit_price']


class AhFile:
    """
    represent json file after extract

    """

    def __init__(self, file):

        self.file = rl.open_json_file(file)
        self.file_name = file
        self.auction_list = self.auctions()
        self.sortfile()
        self.date = ''
        self.id_list = []
        self.list_single_class = []
        self.list_multi_class = []
        self.pandas_data = load_choices_items("items.csv")

    def file_name(self, id_server='test'):
        return "server_" + str(id_server)

    def sortfile(self):
        self.auction_list.sort(key=sort_by_id)

    def auctions(self):
        return self.file['auctions']

    def add_to_multi(self, id_item):
        mutli_object = mul.Items()
        mutli_object.id_items = id_item
        return mutli_object

    def add_to_single(self, row):

        single_object = sin.Item()
        selected_item = self.auction_list[row]

        single_object.id_item = selected_item['item']['id']
        if 'unit_price' in self.auction_list[row]:
            single_object.price_unit = self.auction_list[row]['unit_price']

        elif 'buyout' in self.auction_list[row]:
            single_object.price_buyout = self.auction_list[row]['buyout']
        else:
            single_object.price_buyout = self.auction_list[row]['bid']

        single_object.quantity = selected_item['quantity']
        single_object.time_left = selected_item['time_left']

        single_object.all_data_item = selected_item
        self.list_single_class.append(single_object)
        return single_object

    def get_from_csv_name_by_id(self, id):
        """ function not used """

        id_item = id
        str_id_item = str(id_item)
        with open('items.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['id'] == str_id_item:
                    return row['name item']

    def get_info_from_multi_class_by_id(self, id, name):
        """
        function return items object
        """

        index = bs.search_two(self.list_multi_class, id)

        # put name in class items
        self.list_multi_class[index].item_name = name

        return self.list_multi_class[index]
        # that was before optimization
        # for item in self.list_multi_class:
        #     if item.id_items == id:
        #         item.item_name = name
        #         return item

    def get_from_csv_id_by_name(self, name):
        name_by = name
        name_ = str(name_by)
        with open('items.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            #  first argument is index second is column

            index = bs.binarySearchOnStringPandas(self.pandas_data, name)

            id_by_index = self.pandas_data[index][0]

            return id_by_index
            # for row in reader:
            #
            #     if row['name item'] == name_:
            #         print(row['id'])
            #
            #         return row['id']

    def serch_items(self, name):

        # stworzyc podpowiadanie w wyszukiwaniu
        # print('Search for item: ' + name)

        id = self.get_from_csv_id_by_name(name)
        return self.get_info_from_multi_class_by_id(int(id), name)

    def create_dependency(self):
        """
            main function that is used to form classes item,items
            taking from json parameters, and scraping website to get name of item
        """

        x = 0
        y = 0
        id = self.auction_list[x]['item']['id']
        self.id_list.append(self.auction_list[x]['item']['id'])

        object_items = self.add_to_multi(self.auction_list[x]['item']['id'])
        self.list_multi_class.append(object_items)
        # object_items.item_name = self.get_from_csv_name_by_id(object_items.id_items) bardzo nie optymalne
        object_items.start()

        for i in range(len(self.auction_list)):

            if id == self.auction_list[y]['item']['id']:
                item = self.add_to_single(y)
                object_items.list_item_class.append(item)
                object_items.list_items.append(self.auction_list[y])
                y += 1

            else:

                x = y

                object_items = self.add_to_multi(self.auction_list[x]['item']['id'])
                # object_items.item_name = self.get_from_csv_name_by_id(object_items.id_items)
                object_items.start()

                self.list_multi_class.append(object_items)
                item = self.add_to_single(y)
                object_items.list_item_class.append(item)
                object_items.list_items.append(self.auction_list[y])
                id = self.auction_list[y]['item']['id']
                self.id_list.append(self.auction_list[y]['item']['id'])
                y += 1

    def run(self):

        self.create_dependency()
        anchor = self.serch_items("Anchor Weed")
        return anchor

    def run_same_price(self):
        self.groupSamePriceObjectsAfterSearch()

    def groupSamePriceObjectsAfterSearch(self, name):
        object_items = self.serch_items(name)

        obj_name = object_items.item_name
        obj_id = object_items.id_items
        obj_list = object_items.list_items
        object_items.create_name_without_space()
        # first make if statment to target sort technic
        if object_items.list_item_class[0].price_unit:
            obj_list.sort(key=sort_by_price)

        else:
            obj_list.sort(key=sort_by_buyout)

        counter_first_item = 0
        counter = 0
        list_grouped_items_by_price = []
        p = 0
        q = 0
        runs = 0
        key = return_key(obj_list)
        for item in obj_list:
            runs += 1
            if item[key] == obj_list[counter_first_item][key]:
                counter += 1
                p = item[key]
                q += item['quantity']
            else:
                counter_first_item = counter
                list_grouped_items_by_price.append([p, q])
                p = item[key]
                q = item['quantity']
                counter += 1
        list_grouped_items_by_price.append([p, q])

        object_items.sorted_price_quantity = list_grouped_items_by_price

        return list_grouped_items_by_price


class FileChoice:

    """ obj list these are the elements to add to DB"""

    def __init__(self, objAhFile):
        self.list_with_items_to_del = []
        self.list_with_items_to_add = []
        self.ah_file_obj = objAhFile
        self.choices_obj = []
        # choicesitems are sorted by id, not alphabetical
        self.pandas_model = load_choices_items("choicesitems.csv")
        self.list_selected_id = []
        self.export_id_from_pandas()

    def sort_csv_file_alfabetical(self):
        scv.sort_csv("choicesitems.csv")

    def sort_id_list(self):
        self.list_selected_id.sort()

    def export_id_from_pandas(self):
        """ that must start after loading class"""
        for row in self.pandas_model:
            self.list_selected_id.append(row[0])

    def check_if_record_exist_by_id(self, id_item):
        if bs.search(self.list_selected_id, id_item):
            return True
        else:
            print("item dosn't exist in choiceitems.csv")
            return False

    def session_add(self, list_items):
        for item in list_items:
            self.add_record_to_csv_by_name(item)

    def session_delete(self, list_items_index):
        pandas_scv = pd.read_csv("choicesitems.csv")
        pandas_scv.drop(list_items_index, axis=0, inplace=True)
        pandas_scv.to_csv("choicesitems.csv", index=False)

    def session_delete_by_id(self,):
        """ function not used"""
        for x in range(len(self.list_with_items_to_del)):
            #  NIE DZIALA

            pandas_scv = pd.read_csv("choicesitems.csv")
            pandas_scv = pandas_scv.loc[pandas_scv["id"] == self.list_with_items_to_del[x]]
            print(pandas_scv.shape)
            print(pandas_scv)

            # indexId = pandas_scv[pandas_scv['id'] == id_list[x]]
            # print(indexId)
            # indexId.drop(0)

            # pandas_scv.to_csv("choicesitems.csv", index=False)

    def get_from_csv_id_by_name(self, name):
        index = bs.binarySearchOnStringPandas(self.ah_file_obj.pandas_data, name)
        # first element = id, second element = name, third = url_pic
        id_by_index = self.ah_file_obj.pandas_data[index]
        id_item = id_by_index[0]
        return id_item

    def return_properties_to_add(self, name):
        index = bs.binarySearchOnStringPandas(self.ah_file_obj.pandas_data, name)
        # first element = id, second element = name, third = url_pic
        id_by_index = self.ah_file_obj.pandas_data[index]
        id_item = id_by_index[0]
        name_item = id_by_index[1]
        return id_item, name_item

    def check_if_record_exist_by_name(self, name_item):

        id_item = self.get_from_csv_id_by_name(name_item)

        return self.check_if_record_exist_by_id(id_item)

    def delete_record_from_csv_by_name(self, name_item):

        if self.check_if_record_exist_by_name(name_item):
            print('delete record by: ', name_item)
            index = self.get_index_by_name(name_item)
            self.list_with_items_to_del.append(index)
        else:
            print('not exsits')

    # def delete_record_from_csv_by_id(self, id_item):
    #     """ function not used"""
    #     print(id_item)
    #     if self.check_if_record_exist_by_id(id_item):
    #         # Tutaj ma być zwracany indeks itemu do usuniecia index z choicesitems
    #         index = self.get_index_by_name()
    #         self.list_with_items_to_del.append(index)
    #     else:
    #         print('not exsits')

    def add_record_to_csv_by_name(self, name_item):
        if not self.check_if_record_exist_by_name(name_item):
            print("add new item")
            tuple_item = self.return_properties_to_add(name_item)
            id_item = tuple_item[0]
            item_name = tuple_item[1]
            data = [id_item, item_name]
            print(data)
            with open("choicesitems.csv", 'a') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(data)
                f_object.close()
            scv.sort_csv("choicesitems.csv")

        else:
            print('exsits')

    def add_record_to_csv_by_id(self, id_item):
        print("sprawdzenie czy dany rekord istnieje ", str(id_item))
        if not self.check_if_record_exist_by_id(id_item):
            print("add record by: ", str(id_item))
        else:
            print('exsits')

    def search_for_objs(self):
        for row in self.pandas_model:
            index = bs.search_two(self.ah_file_obj.list_multi_class, row[0])
            if index != -1:
                # if -1 item doesn't exist
                self.choices_obj.append(self.ah_file_obj.list_multi_class[index])
                self.ah_file_obj.groupSamePriceObjectsAfterSearch(row[1])

    def get_index_by_name(self, name):
        index = bs.binarySearchOnStringPandas(self.pandas_model, name)
        return index


# file_test_

# anc = test.groupSamePriceObjectsAfterSearch("Anchor Weed")
# mine = test.groupSamePriceObjectsAfterSearch("Laestrite Ore")
# # arm = test.groupSamePriceObjectsAfterSearch("Desolate Leather Armguards")

def run_test(file_name="test_file.json"):

    test = AhFile(file_name)
    test.create_dependency()
    # test FileChoice
    # run files for class file choice
    te = FileChoice(test)
    # te.search_for_objs()
    te.list_selected_id.sort()
    # run files
    #
    # a = te.check_if_record_exist_by_name("Anchor Weed")
    # aa = te.check_if_record_exist_by_id(152510)

    # print(" get index by name")
    # te.get_index_by_name("Anchor Weed")
    # te.delete_record_from_csv_by_name("Anchor Weed")
    # te.delete_record_from_csv_by_name("17 Pound Catfish")

    # te.session_delete(te.list_with_items_to_del) delete by index

    te.add_record_to_csv_by_name("Laestrite Ore")
    return test

# test = run_test()

# toc = time.perf_counter()
# print(f" Time program runs {toc - tic:0.4f} seconds")
