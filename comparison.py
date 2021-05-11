import read_ah_file_new as raf
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


def sort_by_price(list):
    return list['unit_price']


class Comparison:

    def __init__(self):
        self.list_of_raf_file = []
        self.id_server_compare = 0 #get information about server

    def compare(self, item_to_compare):
        list_of_objects = []
        for raf in self.list_of_raf_file:
            list_of_objects.append(raf.serch_items(item_to_compare))

        # sorting loop

        for x in list_of_objects:
            x.list_items.sort(key=sort_by_price)

        return list_of_objects

    def compare2(self,item_to_compare):
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








com = Comparison()
ah1 = raf.AhFile('ah_1084_03.11.2021_18;42.json')
ah2 = raf.AhFile('ah_1084_03.11.2021_23;03.json')
com.list_of_raf_file.append(ah1)
com.list_of_raf_file.append(ah2)
ah1.create_dependency()
ah2.create_dependency()
w = com.compare('Anchor Weed')
z = com.compare2('Anchor Weed')
