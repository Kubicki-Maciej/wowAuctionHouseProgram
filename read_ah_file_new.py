import realmlist as rl
import item as sin
import items as mul
import csv
import binear_search as bs


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
        """
        find better algorithm searching
        function return items object
        """
        print("przed indexem")
        index = bs.search_two(self.list_multi_class, id)
        print(index)
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

            # binary_s = bs.search_csv(csvfile, name)
            # print(binary_s)

            for row in reader:
                if row['name item'] == name_:
                    print(row)
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

    def run(self):

        self.create_dependency()
        anchor = self.serch_items("Anchor Weed")
        return anchor

    def groupSamePriceObjectsAfterSearch(self, name):
        object_items = self.serch_items(name)

        obj_name = object_items.item_name
        obj_id = object_items.id_items
        obj_list = object_items.list_items
        # first make if statment to target sort technic
        if object_items.list_item_class[0].price_unit:
            obj_list.sort(key=sort_by_price)
            print("sortowanie P")
        else:
            obj_list.sort(key=sort_by_buyout)
            print("sortowanie B")

        counter_first_item = 0
        counter = 0
        list_grouped_items_by_price = []
        p = 0
        q = 0
        runs = 0
        for item in obj_list:
            runs += 1
            if item['unit_price'] == obj_list[counter_first_item]['unit_price']:
                counter += 1
                p = item['unit_price']
                q += item['quantity']
            else:
                counter_first_item = counter
                list_grouped_items_by_price.append([p, q])
                p = item['unit_price']
                q = item['quantity']
                counter += 1
        list_grouped_items_by_price.append([p, q])

        return obj_name, obj_id, obj_list, list_grouped_items_by_price


# file_test_
#
test = AhFile("test_file.json")
a = test.run()
# g = test.groupSamePriceObjectsAfterSearch("Anchor Weed")
