import datetime
from datetime import date
from datetime import datetime
import glob, os
import time

"""

select file by datas and id
1 day all files
7 day one file with closest data
30 days  no data
1 year - no data



"""


def current_date_with_clock():
    fmt = '%m.%d.%Y %H:%M:'
    c_date = datetime.datetime.now()
    data_time = c_date.strftime(fmt)
    return data_time


def current_date():
    c_date = datetime.datetime.now()
    string_date = c_date.strftime("%m.%d.%Y")
    return string_date


def diff_between_dates(file):
    c_d = current_date().split('.')
    f_d = date(int(c_d[2]), int(c_d[0]), int(c_d[1]))
    s_d = date(int(file.year), int(file.month), int(file.day))
    delta = f_d - s_d
    return delta


def compare_day(file):
    d = diff_between_dates(file)
    delta = d.days

    if delta == 0:
        return file.file_name
        print('do magic')


def compare_month(file):
    d = diff_between_dates(file)
    delta = d.days

    if delta < 30:
        print('do magic')


def compare_year(file):
    d = diff_between_dates(file)
    delta = d.days
    if delta < 365:
        print('do magic')


def fresh_file(list_of_file):
    # DO ZROBIENIA
    delta_time_list = []
    current_time = current_date_with_clock()
    for time in list_of_file:
        time_tuple = (time.month, time.day, time.year, time.hours, time.minutes)


current_date_with_clock()




