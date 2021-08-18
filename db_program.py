import comparison as comp
import time
import alchemy_db
import datetime


# rename function
def comparison_file(id_file):
    """
    storage all information about raf files
    load them into base in function name: add_record_to_base_by_file(date, name, raf)
    """
    object_comp = comp.Comparison()
    # first argument means date range witch will load files by id
    object_comp.make_objects_add_them_to_file(2, id_file)
    object_comp.create_dependency_of_ahfile()

    dates = get_date_from_comp(object_comp)
    names = get_names_from_comp(object_comp)
    rafs = get_raf_from_comp(object_comp)

    id_server = object_comp.info_about_item[0][0][1]
    print(id_server)
    # created for test


    # add_record_to_base_file(names, dates)
    for x in range(len(rafs)):
        # check if server exists in base, if not add records
        if alchemy_db.check_if_exists_in_files(names[x]):
            print("dany plik nie istnieje w bazie " + names[x])
            # add_record_to_base_file(names[x], str(dates[x]), id_server) not used
            add_record_to_base_item(dates[x], names[x], rafs[x], id_server)
        else:
            print("file exist in data base")



def comparison_file_test_own_table(id_file):
    """
    returned values are needed to create n item tables database
    """
    object_comp = comp.Comparison()
    # first argument means date range witch will load files by id
    object_comp.make_objects_add_them_to_file(2, id_file)
    object_comp.create_dependency_of_ahfile()

    dates = get_date_from_comp(object_comp)
    names = get_names_from_comp(object_comp)
    rafs = get_raf_from_comp(object_comp)

    id_server = object_comp.info_about_item[0][0][1]
    print(id_server)
    # created for test
    mutli = get_multi_raf(object_comp)
    return mutli, names, dates, id_file



def get_names_from_comp(inserted_object):
    names = []
    for data in inserted_object.info_about_item:
        names.append(data[3])
    return names


def get_date_from_comp(inserted_object):
    dates = []
    for date in inserted_object.info_about_item:
        dates.append(date[0][4])
    return dates

def get_multi_raf(inserted_object):
    rafs = []
    for raf in inserted_object.list_of_raf_file:
        rafs.append(raf.list_multi_class)
    return rafs

def get_raf_from_comp(inserted_object):
    rafs = []
    for raf in inserted_object.list_of_raf_file:
        rafs.append(raf.list_single_class)
    return rafs


def add_record_to_base_file(name, date, id_server):
    tic = time.perf_counter()
    alchemy_db.File_base(name, date, id_server)
    # orm_add(raf, name)
    toc = time.perf_counter()
    print(f" dodawanie do bazy trwało: {toc - tic:0.4f} seconds")


def add_record_to_base_item(date, name, raf, id_server):
    tic = time.perf_counter()
    alchemy_db.Item_base(date, name, raf, id_server)
    # orm_add(raf, name)
    toc = time.perf_counter()
    print(f" dodawanie do bazy trwało: {toc - tic:0.4f} seconds")


# t = comparison_file_test_own_table(1084) used to test multipletabletodatabase

