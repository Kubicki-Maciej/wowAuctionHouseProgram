import glob, os
import realmlist as rl


def load_file(id_server):
    os.chdir("E:/WoWprogram/" + str(id_server))
    temp_file_list = []
    for file in glob.glob("*.json"):
        temp_file_list.append(file)

    return temp_file_list


def objects_file(loaded_files):
    temp_object_list = []
    for file in loaded_files:
        temp_object = File(file)
        temp_object_list.append(temp_object)
    return temp_object_list


"""
os.chdir("F:/WoWAuctionApi/1084")
list_file = []

for file in glob.glob("*.json"):
    list_file.append(file)
    print(file)

w = rl.list_class_server
"""


class File:

    def __init__(self, file_name):
        self.file_name = file_name
        self.id_ah = 0
        self.data = 0
        self.time = 0
        self.realm_list_object = self.realm_list(rl.list_class_server)

        self.day = 0
        self.month = 0
        self.year = 0

        self.hours = 0
        self.minutes = 0

        self.split_file_name()

    def split_file_name(self):
        # split file
        split_file = self.file_name.split("_")
        self.id_ah = int(split_file[1])
        self.data = split_file[2]
        # split data
        data_split = self.data.split(".")
        self.day = int(data_split[1])
        self.month = int(data_split[0])
        self.year = int(data_split[2])

        remove_json = split_file[3]
        self.time = remove_json[:-5]

        time_split = self.time.split(";")
        self.hours = int(time_split[0])
        self.minutes = int(time_split[1])

    def realm_list(self, realm_list):
        for realm in realm_list:
            if self.id_ah == realm.id_group:
                return realm

# pobiera dane z sciezki gdzie liczba to numer servera

# obj_files = objects_file(load_file(1084))
