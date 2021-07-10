import read_ah_file_new as raf
import itemsgui
import math


def return_key(objectList):

    if ('unit_price') in objectList[0]:
        key = 'unit_price'
    else:
        key = 'buyout'
    return key


def n_number(number):
    # rounding number
    min_number = number * -1
    ceil_number = math.ceil(min_number)
    number_to_return = ceil_number * -1
    return number_to_return


def testing():
    opened_json_object = raf.AhFile('test_file.json')
    opened_json_object.create_dependency()
    itemsObjectList = opened_json_object.serch_items('Anchor Weed')
    itemsObjectList.list_items.sort(key=raf.sort_by_price)
    items_object = itemsgui.ItemBox(itemsObjectList.list_items)

    id_item_from_serch = items_object.item_list[0]['item']['id']
    item_name = itemsObjectList.item_name

    return itemsObjectList, item_name, id_item_from_serch


def min_value(itemsObjList):
    key = return_key(itemsObjList)
    return itemsObjList[0][key]


def average_price(itemsObjList):
    """ to return average price take element[4]"""

    quantity_list = []
    price_list = []
    price_multiply_by_quantity = []

    key = return_key(itemsObjList)

    for x in range(len(itemsObjList)):
        quantiy = itemsObjList[x]['quantity']
        price = itemsObjList[x][key]

        quantity_list.append(quantiy)
        price_list.append(price)

        price_multiply_by_quantity.append(price * quantiy)

    sum_price = sum(price_multiply_by_quantity)
    sum_quantity = sum(quantity_list)

    avrage_item_price = sum_price / sum_quantity
    rounded_avg_price = n_number(avrage_item_price)

    return quantity_list, price_list, price_multiply_by_quantity, avrage_item_price, rounded_avg_price, split_value(
        rounded_avg_price)


def take_average_price_first_x_items(itemsObjList, value_takenStr):
    print("enter take avg price")
    value_taken = int(value_takenStr)
    checkboolean = value_to_high(value_taken, itemsObjList)
    if checkboolean:
        # y - is counter to compare
        y = 0
        quantity_list = []
        price_list = []
        price_multiply_by_quantity = []
        key = return_key(itemsObjList)
        print(key)

        for x in range(len(itemsObjList)):
            quantiy = itemsObjList[x]['quantity']
            price = itemsObjList[x][key]
            print(price)

            price_list.append(price)

            if value_taken <= y + quantiy:

                number_items_left = value_taken - y
                quantity_list.append(number_items_left)
                price_multiply_by_quantity.append(number_items_left * price)
                break

            else:
                quantity_list.append(quantiy)
                price_multiply_by_quantity.append(price * quantiy)
                y += quantiy

        sum_price = sum(price_multiply_by_quantity)
        sum_quantity = sum(quantity_list)
        avrage_item_price = sum_price / sum_quantity
        cost_of_x_items = avrage_item_price * value_taken
        return price_multiply_by_quantity, price_list, quantity_list, avrage_item_price, cost_of_x_items, split_value(
            int(avrage_item_price))
    else:
        # return quantity * price
        quantity_list = []
        price_list = []
        price_multiply_by_quantity = []

        key = return_key(itemsObjList)
        for x in range(len(itemsObjList)):
            quantiy = itemsObjList[x]['quantity']
            price = itemsObjList[x][key]

            quantity_list.append(quantiy)
            price_list.append(price)
            price_multiply_by_quantity.append(price * quantiy)

        sum_price = sum(price_multiply_by_quantity)
        sum_quantity = sum(quantity_list)
        avrage_item_price = sum_price / sum_quantity
        return price_multiply_by_quantity, price_list, quantity_list, avrage_item_price, 0, split_value(
            int(avrage_item_price))


def value_to_high(value_to_check, itemsObjList):
    functionAvrage = average_price(itemsObjList)

    if sum(functionAvrage[0]) < value_to_check:
        print('podano zaduża wartość ERROR')
        return False
    return True


""" do zrobenia pobierz srednia ilosc do wydania golda """


def buy_by_x_gold_amount(value_taken, itemsObjList):
    quantity_list = []
    price_list = []
    price_multiply_by_quantity = []
    number_of_items = 0
    average_price = 0
    key = return_key(itemsObjList)
    for x in range(len(itemsObjList)):
        quantiy = itemsObjList[x]['quantity']
        price = itemsObjList[x][key]

        price_quantity = price * quantiy
        price_multiply_by_quantity.append(price_quantity)

        if value_taken < sum(price_multiply_by_quantity):

            gold_left = (value_taken - sum(price_multiply_by_quantity)) * -1
            items_left = quantiy - (gold_left / price)

            quantity_list.append(items_left)
            price_list.append(price)
            # u can't buy half of item
            number_of_items = sum(quantity_list)
            # function that return naturalnumber
            items = n_number(number_of_items)

            break
        else:
            quantity_list.append(quantiy)
            price_list.append(price)

    return quantity_list, price_list, price_multiply_by_quantity, items


def split_value(value):
    strvalue = str(value)
    sac, gold = strvalue[-4:], strvalue[:-4]
    silver = sac[:2]
    copper = sac[2:]
    return_value = (gold + "g" + silver + "s" + copper + "c")
    return return_value
    # return gold, silver, copper


def avg_percent_items_price(percentStr, itemsObjList):
    avg = average_price(itemsObjList)
    percent = int(percentStr)
    avg_price = avg[4]
    percent_avg_price = percent / 100 * avg_price

    quantity_list = []
    price_list = []
    price_multiply_by_quantity = []
    key = return_key(itemsObjList)
    for x in range(len(itemsObjList)):

        quantiy = itemsObjList[x]['quantity']
        price = itemsObjList[x][key]

        if percent_avg_price <= price:
            break
        else:
            quantity_list.append(quantiy)
            price_list.append(price)
            price_multiply_by_quantity.append(price * quantiy)

    sum_price = sum(price_multiply_by_quantity)
    sum_quantity = sum(quantity_list)

    avrage_item_price = sum_price / sum_quantity
    rounded_avg_price = n_number(avrage_item_price)

    return split_value(str(avrage_item_price)), split_value(
        str(rounded_avg_price)), quantity_list, price_list, price_multiply_by_quantity

# avg price do ceny jakies per item proste

#
# test = testing()
#
# w = test[0].list_items
# g = average_price(w)
#
# io = buy_by_x_gold_amount(200000, w)
# xo = avg_percent_items_price(150, w)
