from time import sleep
from threading import Thread
import apiconnect as api
import realmlist as rl


def func(list_of_server):
    """
    download files from blizzard api by id in Json
    """
    for realm in list_of_server:
        try:
            directory = api.create_new_folder(realm.id_group)
            api.auction_house_download(realm.id_group, directory)
            # print('download json file id:' + str(realm.id_group))
        except:
            print("error with download file id :" + str(realm.id_group))
    print('downloads success')

def download_all_servers():
    func(rl.list_class_server)



def downloadFunction(server_id):
    # create new folder to save data
    directory = api.create_new_folder(server_id)
    api.auction_house_download(server_id, directory)



w = rl.list_class_server
# while True:
#     directory = api.create_new_folder()
#     Thread(target=func(rl.list_class_server, directory)).start() #download files every 1h:10m
#
#     sleep(4200)
