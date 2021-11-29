import realmlist  # first realmlist execute then apiconnect !!!
# import wowapi
import json
import os
import datetime
from blizzardapi import BlizzardApi

key = '0d7282069bad432c8cac95125523f7cf'
secretkey = 'wLcGwQgP72kzpMzH81I8siD4UbZTlH2f'

api_client = BlizzardApi(key, secretkey)


def current_date():
    """ return date m/d/y/h/m/ """
    current_date = datetime.datetime.now()
    string_date = current_date.strftime("%m.%d.%Y_%H;%M")
    return string_date

def save_file_json(file_to_save, id_group_server, directory):
    """ save downlaoded file, taking arg id_group_server """

    with open('data/Json/'+directory+'/'+'ah_' + str(id_group_server) + '_' + current_date() + '.json', 'w') as json_file:
        print("save json file")
        json.dump(file_to_save, json_file,) #indent=2)

def create_new_folder(id_server):
    """ create new folder where data from api came in"""
    try:
        directory = str(id_server)
        parent_dir = os.getcwd() +"\data\Json"
        # print('make path '+ str(id_server))
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)
        #print('created file :'+directory)
        print(directory)
        return directory

    except FileExistsError:
        print("file with this name exist skip creating it")
        directory = str(id_server)
        print(directory)
        return directory

def auction_house_download(id_group_server, directory, region='eu', dynamic='dynamic-eu'):
    """ send request to get auction house file, saveing it in Json with current date """

    json_ah_file = api_client.wow.game_data.get_auctions(region, dynamic, id_group_server)
    save_file_json(json_ah_file, id_group_server, directory)
    print(current_date()+' pobrano auction house')


def download_item_by_id(id_item):
    """
    function connect to blizzard server and download item_data and item_media where is icon of item
    :param id_item:
    :return: information about item, picture item
    """
    item_data = api_client.wow.game_data.get_item('eu','static-eu', id_item)
    item_media_data = api_client.wow.game_data.get_item_media('eu','static-eu', id_item)
    return item_data, item_media_data