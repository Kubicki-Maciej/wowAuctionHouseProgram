import csv
import pandas as pd
import read_ah_file as ah_file

"""
main function -> run()
datasave is for serching new items in list_multi_class 
if is a new item add it to items.csv 
"""

def create_file(namefile):

    with open(namefile, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id','name item','url pict'])

def save_to_file(filename, data):

    with open(filename, 'a') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(data)

def make_pd_file(filename):
    file = pd.read_csv(filename)
    return file

def check_true(file,idlist):
    """ zrobic funkcje z bierzaca wszystkie id ? """
    res2 = {elem: True if elem in file.values else False for elem in idlist}
    return res2

log_list =[]
log_e_list = []

def run(main_file = 'items.csv'):
    """ elementów których nie ma laduja w liscie list multi ? czy pierw
    sprawdza wszystko ?
    plik kiedy wchodzi nowa lista ?
    """
    file_pd = make_pd_file(main_file)

    boolean_list_id_false = check_true(file_pd, ah_file.id_list) # id| boolean
    print(boolean_list_id_false)
    #number_itmes = (len(boolean_list_id_false))
    #print(number_itmes)
    #print(len(ah_file.list_multi_class))
    i = 0
    for x in boolean_list_id_false:
        try:
            if boolean_list_id_false[x] == False:
                """ adding to list serched id """
                #print(str(x)+ ' '+str(boolean_list_id_false[x]))
                items = ah_file.list_multi_class[i]
                items.get_name_from_bn()

                data = [items.id_items, items.item_name, items.picture_url] # info to save first id|item_name
                print("dodano "+str(data))
                save_to_file(main_file, data)

            else:
                log_list.append(
                    'element jest w liscie ' + str(x) + ' ' + str(boolean_list_id_false[x])
                )
            i += 1
        except:
            print("error , skip adding item to list ID_ITEM:"+ str(items.id_items))
            log_e_list.append(str(items.id_items))

            i += 1
    save_to_file('error_log.csv', log_e_list)
    print('operation download file done')

#run('items.csv')
#127761, 178131

