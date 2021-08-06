"""
zapisywanie daty do plików Json, csv, DB
sprawdzenie czy dane id istnieje jak tak nie zapisywać
UDOSKONALIC TO
"""
import os
import csvsort
import sqlite3
import csv
import pandas as pd
import read_ah_file as ah_file
import requests
import json

log_list = []
log_e_list = []


def create_file(namefile):
    """ create csv file """
    with open(namefile, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id','name item','url pict'])
        # writer.writerow(['setting name','int_value','boolean','str_value'])


def save_to_file(filename, data):
    """ save to filename.csv <- data """
    with open(filename, 'a') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(data)


def make_pd_file(filename):
    """ read file by pandas """
    file = pd.read_csv(filename)
    return file



def read_csv_f(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)



def check_true(file,idlist):
    """ sprawdza czy sa dane id jezeli nie ma, zwraca brakujace """
    res2 = {elem: True if elem in file.values else False for elem in idlist}
    return res2


def select_data_base_and_print(data_base):
    """ print all rows in db"""
    conn = sqlite3.connect(data_base)
    c = conn.cursor()
    c.execute("SELECT * FROM items")

    rows = c.fetchall()
    for row in rows:
        print(row)

    conn.close()
#select_data_base_and_print('dataitems.db')


# dataitems.db basic name of db
def create_table(data_base):
    """ create table """
    conn = sqlite3.connect(data_base)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS items (
        id_item integer,
        item_name text,
        picture_url text
    )""")
    conn.commit()
    conn.close()


def add_new_record(data_base, id_item, item_name, picture_url):
    """ add new record to data base
    values:
    id_item, item_name, picture_url
    """
    conn = sqlite3.connect(data_base)
    c = conn.cursor()
    # c.execute("SELECT INTO items VALUES (?,?,?)", (id_item, item_name, picture_url))
    c.execute("INSERT INTO items VALUES (:id_item, :item_name, :picture_url)",
              {
                  'id_item': id_item,
                  'item_name': item_name,
                  'picture_url': picture_url,
              })

    #print("dodano do bazy danych "+str(id_item) + " " + item_name + " " + picture_url )

    conn.commit()
    conn.close()
#add_new_record('dataitems.db','test','test','test')

def serch_in_db(item_id_s , data_base = 'dataitems.db'):
    conn = sqlite3.connect(data_base)
    c = conn.cursor()

    c.execute("SELECT * FROM items WHERE id_item=:id_item",
              {
                  'id_item': item_id_s
               })

    conn.commit()
    conn.close()


def run(main_file = 'items.csv', data_base='dataitems.db'):
    """ elementów których nie ma laduja w liscie list multi ? czy pierw
    sprawdza wszystko ?
    plik kiedy wchodzi nowa lista ?


    adding from read_ah_file records to db and csv file
    """
    file_pd = make_pd_file(main_file)

    boolean_list_id_false = check_true(file_pd, ah_file.id_list) # id| boolean
    #print(boolean_list_id_false)
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

                #csv add
                data = [items.id_items,
                        items.item_name,
                        items.picture_url]


                # save to temp file to download images
                save_to_file('temp_items.csv', data)

                #print("dodano "+str(data))
                save_to_file(main_file, data) # save to csv

                #database add
                add_new_record(data_base,items.id_items,
                               items.item_name,
                               items.picture_url) # save to db

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

def download_jpg_by_id(item_id_s):
    """ downloads by db system """
    conn = sqlite3.connect('dataitems.db')
    c = conn.cursor()
    c.execute("SELECT * FROM items WHERE id_item=:id_item",
              {
                  'id_item': item_id_s
               })

    g = c.fetchall()

    for item in g:
        print(item[0], item[1])
        idItem = item[0]
        jpgItem = item[1]
        download_single_jpg(idItem, jpgItem)
    c.close()
    return g

def download_jpgs():
    """
    download jpgs by csv
    """

    # add new download from csv
    file = load_csv_file('temp_items.csv')


    for x in range(len(file)):
        row = file.iloc[x]
        idItem = row['id']
        jpgItem = row['url pict']
        download_single_jpg(idItem, jpgItem)
    # c.close()

def download_single_jpg(id, url):
    print('downloading ' + str(id) + " " + url)
    response = requests.get(url)
    file = open("data/img/itemsimg/"+str(id)+".jpg", "wb")
    file.write(response.content)
    file.close()

def load_csv_file(file_name):
    data = pd.read_csv(file_name)
    df = pd.DataFrame(data,columns=['id','url pict'])

    return df

def create_temp_file():
    create_file("temp_file.csv")


def main():
    """ after run() we got temp file when we need to execute it to download pictures """
    if os.path.exists("temp_items.csv"):
        os.remove("temp_items.csv")
    else:
        print("does not exist")
    create_temp_file()
    run()
    download_jpgs()


