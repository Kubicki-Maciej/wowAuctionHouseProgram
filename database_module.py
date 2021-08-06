"""
connect with date base
1) check if this file exist if not:
    selected items (from selected.csv) and save them in DB
if exist:
    compere selected.csv db "file_name" if are new items add them to database

script should run in evry create items.py ? read_ah_file_new.py in create_dependecy ?? or should be created new in raf
new dependecy and from there should be taken arguments

"""
# na chwile obecna nieuzywany zmieniony na alchemy_db i db_program
from psycopg2.sql import SQL

import read_ah_file_new as raf
import psycopg2
from psycopg2 import sql
import pandas as pd
import numpy as np
from pandas import DataFrame
import sqlite3


def create_local_db_items():
    conn = sqlite3.connect('data_items.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS items (
        id_item integer,
        item_name text,
        picture_url text,
        url text
    )""")


class DataBase:

    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = psycopg2.connect(database=db_name, user="postgres", password="war", host="127.0.0.1", port="5432")
        self.curs = self.conn.cursor()
        self.tables_names = self.get_all_tables_name()

    def get_all_tables_name(self):
        self.curs.execute("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")
        return self.curs.fetchall()

    def execute_query(self, q):
        self.curs.execute(q)
        return self.curs.fetchall()

    def execute_query_with_arg(self, q, arg):
        self.curs.execute(q, arg)
        return self.curs.fetchall()

