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
    """ return date m/d/y/h/m/s """
    current_date = datetime.datetime.now()
    string_date = current_date.strftime("%m_%d_%Y_%H_%M_%S")
    return string_date


def save_file_json(file_to_save, id_group_server):
    """ save downlaod file, taking arg id_group_server """
    with open('ah_' + str(id_group_server) + '_' + current_date() + '.json', 'w') as json_file:
        json.dump(file_to_save, json_file,) #indent=2)


def auction_house_download(id_group_servers, region='eu', dynamic='dynamic-eu'):
    """ send request to get auction house file, saveing it in Json with current date """

    json_ah_file = api_client.wow.game_data.get_auctions(region, dynamic, id_group_servers)
    save_file_json(json_ah_file, id_group_servers)
    print(current_date()+' pobrano auction house')
    return json_ah_file

def download_item_by_id(id_item):
    """
    function connect to blizzard server and download item_data and item_media where is icon of item
    :param id_item:
    :return: information about item, picture item
    """
    item_data = api_client.wow.game_data.get_item('eu','static-eu', id_item)
    item_media_data = api_client.wow.game_data.get_item_media('eu','static-eu', id_item)
    return item_data, item_media_data