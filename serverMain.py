from time import sleep
from threading import Thread
import apiconnect as api

def func():
    """
    server functions
    import files from blizzard api

    :return:
    """
    api.auction_house_download(1084) #id tarenmill



while True:
    """
    download files every 1h:10m
    """
    Thread(target=func()).start()
    sleep(4200)
