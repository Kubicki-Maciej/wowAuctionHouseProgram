from tkinter import *
import time


class ItemsGui:

    def __init__(self, object, row_p, row_q, column_p, column_q, value_p, value_q):
        self.object = object
        self.row_p = row_p
        self.row_q = row_q
        self.column_p = column_p
        self.column_q = column_q
        self.value_p = value_p
        self.value_q = value_q
        self.price_box = None
        self.quantity_box = None

    def start(self, root):
        self.price_box = Label(root, text=self.value_p).grid(row=self.row_p, column=self.column_p)
        self.quantity_box = Label(root, text=self.value_q).grid(row=self.row_q, column=self.column_q)

class ItemBox:

    def __init__(self, objects_items):
        self.item_list = objects_items
        self.split_list_items = []
        self.items_gui_objects = []

    """
        maskymalnie moze byc wyswietlane 8 przedmiotow 

    """

    def split_list(self):
        """counter - elements of list to display"""

        counter = 0
        temp_list = []
        for item in self.item_list:

            if counter < 15:
                temp_list.append(item)
                counter += 1
            else:
                self.split_list_items.append(temp_list)

                temp_list = []
                temp_list.append(item)

                counter = 1
        if len(temp_list) > 0:
            self.split_list_items.append(temp_list)

    def box_items(self, root, values):
        """ adding labels to root Tk()"""



        items_gui_objects = []
        v_row = 6
        v_column_p = 3
        v_column_q = 4

        price_box = Label(root, text="Price per item").grid(row=5, column=v_column_p)
        quantity_box = Label(root, text="quantity").grid(row=5, column=v_column_q)

        for items in values:
            create_object = ItemsGui(items, v_row, v_row, v_column_p, v_column_q, self.unit_price_buyout_bid(items),
                                     items['quantity'])
            create_object.start(root)
            items_gui_objects.append(create_object)
            v_row += 1





    def start_box_items(self, list_number):
        return self.split_list_items[list_number]

    def split_value(self, value):
        strvalue = str(value)
        sac, gold = strvalue[-4:], strvalue[:-4]
        silver = sac[:2]
        copper = sac[2:]
        return_value = (gold + "g" + silver + "s" + copper + "c")
        return return_value
        # return gold, silver, copper

    def unit_price_buyout_bid(self, values):

        if 'unit_price' in values:
            formatted_value = values['unit_price']
        elif 'buyout' in values:
            formatted_value = values['buyout']
        else:
            formatted_value = values['bid']

        return self.split_value(formatted_value)
