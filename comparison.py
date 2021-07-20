import read_ah_file_new as raf
import select_file_by_date as sfd
import mathprice
import os

"""
for x in range(len(w[0].list_items)):
...     if w[0].list_items[x]['unit_price'] > (avg * 3) or w[0].list_items[x]['unit_price'] < (avg * 0.15):
...         
...         print('nie przechodzi')
...     else:
...         print('przechodzi')        
"""


def summ_all(list1, list2):
    if len(list1) == len(list2):
        temp_list = []
        for x in range(len(list1)):
            price = list1[x]
            quant = list2[x]
            summ = price * quant
            temp_list.append(summ)
        return temp_list


def sort_by_buyout(list):
    return list['buyout']


def sort_by_price(list):
    return list['unit_price']


class Comparison:

    def __init__(self):
        self.info_about_item = []
        self.list_of_raf_file = []
        self.list_min_price = []
        self.list_avg_price = []
        self.object_from_compare = None;
        self.id_server_compare = 0  # get information about server

    def compare(self, item_to_compare):
        self.create_dependency_of_ahfile()

        list_of_objects = []

        counter = 0
        for raf in self.list_of_raf_file:
            item = self.list_of_raf_file[counter].serch_items(item_to_compare)

            list_of_objects.append(item)

            counter += 1

        for x in list_of_objects:

            if 'unit_price' in list_of_objects[0].list_items[0]:
                x.list_items.sort(key=sort_by_price)
                print('sort UP')

            elif 'buyout' in list_of_objects[0].list_items[0]:
                print(x.list_items)
                x.list_items.sort(key=sort_by_buyout)
                print("sort BO")

        self.object_from_compare = list_of_objects

        return list_of_objects

    def compare2(self, item_to_compare):
        compare1 = self.compare(item_to_compare)

        for items in compare1:
            list_price = []
            list_qunatity = []

            for item in items.list_item_class:
                list_qunatity.append(item.quantity)
                list_price.append(item.price_unit)

            value_market = summ_all(list_price, list_qunatity)

            print(sum(value_market))
            return sum(value_market)

    def create_object_raf(self, path):
        created_object = raf.AhFile(path)
        return created_object

    def load_same_id_by_date(self, selected_option, id_server):
        selectedFiles = sfd.get_files_by_id(id_server)
        newest_files = sfd.newest_file(selectedFiles)
        tempfile = []
        for one_file in newest_files[0]:

            if one_file[2][selected_option]:
                self.info_about_item.append(one_file)
                tempfile.append(one_file)
        print(str(len(tempfile)))
        return tempfile

    def make_objects_add_them_to_file(self, selected_option, id_server):
        """add to list_of_raf_file information about """
        list_of_tuples = self.load_same_id_by_date(selected_option, id_server)
        for one_file in list_of_tuples:
            print(one_file[4])
            self.list_of_raf_file.append(self.create_object_raf(one_file[4]))

    def create_dependency_of_ahfile(self):
        for x in self.list_of_raf_file:
            x.create_dependency()

    def make_avg_percent_price(self, valuepercent):
        temp_percent = []
        for object_list in self.object_from_compare:
            ap = mathprice.avg_percent_items_price(150, object_list.list_items)
            temp_percent.append(ap[1])
        return temp_percent

    def make_average_price_first_x_items(self, value=100):
        temp_list_avg_first_x_items = []
        for object_list in self.object_from_compare:
            tapfi = mathprice.take_average_price_first_x_items(object_list.list_items, value)
            print(tapfi)
            temp_list_avg_first_x_items.append(tapfi[5])
        return temp_list_avg_first_x_items

    def min_price(self):
        temp_min_price = []
        for object_list in self.object_from_compare:
            mv = mathprice.min_value(object_list.list_items)
            self.list_min_price.append(mv)
            temp_min_price.append(mathprice.split_value(mv))

        return temp_min_price

    def avg_price(self):
        temp_avg_price = []
        for object_list in self.object_from_compare:
            lap = mathprice.average_price(object_list.list_items)
            self.list_avg_price.append(lap)
            temp_avg_price.append(lap[5])
        return temp_avg_price


# if some option is selected load files only with true in test[0][2]
# where element 0 is today element 1 is week, 2 element is month
#
# def load_file_by_selected_option_same_id(return_option, select_file_by_id):
#     temp_file_list = []
#     for one_file in select_file_by_id[0]:
#         if one_file[2][return_option]:
#             print("dodaje do systemu ")
#             temp_file_list.append(one_file)
#
#     return temp_file_list
#
# selectedFiles = sfd.get_files_by_id(1084)
# test = sfd.newest_file(selectedFiles)
def test():
    com = Comparison()
    com.make_objects_add_them_to_file(1, 1084)
    # zwraca liste itemów na x mozna robic dzialania
    x = com.compare('Anchor Weed')

    # średnia cena
    avg = mathprice.average_price(x[0].list_items)
    # minimalna cena
    min = mathprice.min_value(x[0].list_items)

    return com, x, avg, min
