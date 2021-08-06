import datetime
from datetime import date
from datetime import datetime
from datetime import timedelta
import glob, os
import time
from os.path import isfile, join
from os import listdir


# program_path = os.getcwd()
# my_path = program_path + '\data\Json'
#
# files = os.listdir(my_path)
# onlyfiles = [f for f in listdir(my_path) if isfile(join(my_path, f))]

# add to my_path '\id to get folder with json files

def make_path(id_server):
    path_of_main_folder = os.getcwd() + '\data\Json'
    path_by_id = os.path.join(path_of_main_folder, str(id_server))
    return path_by_id


def get_files_by_id(id_server):
    """ return path to json file in list form single id used to create newest fiele"""
    try:
        path_of_main_folder = os.getcwd() + '\data\Json'
        path_by_id = os.path.join(path_of_main_folder, str(id_server))
        list_of_files = os.listdir(path_by_id)
        return list_of_files
    except:
        print('Error no file in data/json/'+str(id_server))

def create_class_date_from_file(file, x=0):
    splited_file = file.split('_')
    typeOfFile = splited_file[0]
    server_id = splited_file[1]
    downloadDate = splited_file[2]
    tempTime = splited_file[3].split('.')
    downloadTime = tempTime[0]

    splitedDate = downloadDate.split('.')
    splitedTime = downloadTime.split(';')

    create_date_object = datetime(int(splitedDate[2]), int(splitedDate[0]), int(splitedDate[1]), int(splitedTime[0]),
                                  int(splitedTime[1]))
    if x == 0:
        return create_date_object
    else:
        return typeOfFile, server_id, downloadDate, downloadTime, create_date_object


def currentDate():
    return datetime.now()


def delta_time(currentDate, file_name):
    delta = currentDate - file_name
    return delta


def current_date_with_clock():
    fmt = '%m.%d.%Y %H:%M'
    c_date = datetime.now()
    data_time = c_date.strftime(fmt)
    return data_time


def current_date():
    c_date = datetime.now()
    string_date = c_date.strftime("%m.%d.%Y")
    return string_date


def diff_between_current_and_taken_date(file):
    c_d = current_date().split('.')
    f_d = date(int(c_d[2]), int(c_d[0]), int(c_d[1]))
    s_d = date(int(file.year), int(file.month), int(file.day))
    delta = f_d - s_d
    return delta


def same_day(file):
    d = diff_between_current_and_taken_date(file)
    delta = d.days

    if delta <= 0:

        # print(' D')
        return True
    else:
        return False


def compare_7days(file):
    d = diff_between_current_and_taken_date(file)
    delta = d.days

    if delta < 7:
        # print(' W')
        return True
    else:
        return False


def compare_m(file):
    d = diff_between_current_and_taken_date(file)
    delta = d.days
    if delta < 30:
        # print(' M')
        return True
    else:
        return False


def check_when_made(date_objc):
    first = same_day(date_objc)
    second = compare_7days(date_objc)
    third = compare_m(date_objc)

    return first, second, third


def newest_file(all_files):
    temp_list_objc_data = []
    temp_list_delta = []
    temp_tuple = []
    big_list = []

    counter = 0

    for file in all_files:
        obj_ = create_class_date_from_file(file, 1)
        temp_list_objc_data.append(obj_)

        delt_ = delta_time(currentDate(), temp_list_objc_data[counter][4])
        temp_list_delta.append(delt_)
        # funkcja zwracajaca krotke ze sprawdzeniem kiedy ten plik powstał
        bool_tuple = check_when_made(temp_list_objc_data[counter][4])
        temp_tuple.append(bool_tuple)

        path_to_file = os.path.join(make_path(obj_[1]), file)

        big_list.append((obj_, delt_, bool_tuple, file, path_to_file))

        counter += 1

    newest_file = big_list[-1]

    return big_list, newest_file


def sorted_freshfile(list_data):
    pass


def fresh_file(list_of_file):
    # DO ZROBIENIA
    delta_time_list = []
    current_time = current_date_with_clock()
    for time in list_of_file:
        time_tuple = (time.month, time.day, time.year, time.hours, time.minutes)


# current_date_with_clock()


test = newest_file(get_files_by_id(1084))
#  do zrobienia najnowszy plik , w gui zrobienie automatycznego wyboru najnowszego pliku
#  chyba ze zostal wybrany inny plik, pobieranie z settings informacji o id servera który ma zostać wyświetlony na
# głównej stronie
