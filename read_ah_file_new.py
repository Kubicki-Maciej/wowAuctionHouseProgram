import realmlist as rl
import item as sin
import items as mul
import csv


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
        self.file_name()
        self.auction_list = self.auctions()
        self.sortfile()
        self.date = ''
        self.id_list = []
        self.list_single_class = []
        self.list_multi_class = []

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
        """ find better algoritm serching
        function return items object
        """
        for item in self.list_multi_class:
            if item.id_items == id:
                item.item_name = name
                return item
                print(item)

    def get_from_csv_id_by_name(self, name):
        name_by = name
        name_ = str(name_by)
        with open('items.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['name item'] == name_:
                    return row['id']

    def serch_items(self, name):
        # stworzyc podpowiadanie w wyszukiwaniu
        print('Search for item: ' + name)

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
