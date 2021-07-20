"""
connect with date base
1) check if this file exist if not:
    selected items (from selected.csv) and save them in DB
if exist:
    compere selected.csv db "file_name" if are new items add them to database

script should run in evry create items.py ? read_ah_file_new.py in create_dependecy ?? or should be created new in raf
new dependecy and from there should be taken arguments

"""

import psycopg2
from psycopg2 import sql
import pandas as pd
import numpy as np
from pandas import DataFrame


# here import from list_items and push as once all items

class DataBase:

    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = psycopg2.connect(database=db_name, user="postgres", password="war", host="127.0.0.1", port="5432")
        self.curs = self.conn.cursor()

    # https://www.postgresqltutorial.com/postgresql-python/create-tables/
    def checkIfTableExsist(self):
        """
        if table not exist run create Table With File Name
        if exist check data in tables compare it
        """
        pass

    def createTableWithFileName(self, filename):

        comands = (
            "    CREATE TABLE (%s)   " % filename

        ),
        print(comands)
    def compareDateInTableAndModels(self):
        pass
        #sql2 = """INSERT INTO group_server (name_group, group_number, id) VALUES (%s, %s, %s) WHERE NOT EXISTS (SELECT * FROM group_server WHERE id = (%s)"""
        # data = (1085, "silver", 2, 1085)
        #        self.curs.execute(sql2, data)

test_base = DataBase("testah")
