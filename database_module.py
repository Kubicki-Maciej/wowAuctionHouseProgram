"""
connect with date base
1) check if this file exist if not:
    selected items (from selected.csv) and save them in DB
if exist:
    compere selected.csv db "file_name" if are new items add them to database

script should run in evry create items.py ? read_ah_file_new.py in create_dependecy ?? or should be created new in raf
new dependecy and from there should be taken arguments

"""

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


# sciagawka
# cur.execute(
#     sql.SQL("insert into {} values (%s, %s)")
#         .format(sql.Identifier('my_table')),
#     [10, 20])


# query = sql.SQL("select {field} from {table} where {pkey} = %s").format(
#     field=sql.Identifier('my_name'),
#     table=sql.Identifier('some_table'),
#     pkey=sql.Identifier('id'))

# here import from list_items and push as once all items

class DataBase:

    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = psycopg2.connect(database=db_name, user="postgres", password="war", host="127.0.0.1", port="5432")
        self.curs = self.conn.cursor()
        self.tables_names = self.get_all_tables_name()

    # https://www.postgresqltutorial.com/postgresql-python/create-tables/
    def checkIfTableExists(self):
        """
        if table not exist run create Table With File Name
        if exist check data in tables compare it
        """
        pass

    def create_file_name_table(self):
        command = (
            """
            CREATE TABLE IF NOT EXISTS file_names
            (
            id_file serial NOT NULL,
            file_name varchar(90) NOT NULL,
            id_group_servers integer NOT NULL,
            file_date DATE,
            create_date DATE NOT NULL DEFAULT CURRENT_DATE,
            PRIMARY KEY (id_file)
            )
            """
        )
        try:
            self.curs.execute(command)
            self.curs.close()
            self.conn.commit()
            print("created ", command)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()

    def create_item_name_table(self, item_from_raf_without_space):
        """ create table name by item name """
        try:
            self.curs.execute(
                sql.SQL("""
                        CREATE TABLE IF NOT EXISTS{}
                        (
                        id_file integer NOT NULL,
                        quantity integer NOT NULL,
                        price integer NOT NULL,             
                        item_name varchar(150),
                        FOREIGN KEY (id_file)
                            REFERENCES file_names (id_file)
                            ON UPDATE CASCADE ON DELETE CASCADE
                        )
                        """).format(sql.Identifier(item_from_raf_without_space))
            )
            self.curs.close()
            self.conn.commit()
            print("should create table ", item_from_raf_without_space)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()

    def insert_into_file_names(self, data, table_name='file_names'):
        self.curs.execute(
            sql.SQL("INSERT INTO {} VALUES (%s, %s, %s, %s, %s)").format(sql.Identifier(table_name)),
            data
        )

    def get_all_tables_name(self):

        self.curs.execute("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")
        return self.curs.fetchall()

    def compareDateInTableAndModels(self):
        pass
        # sql2 = """INSERT INTO group_server (name_group, group_number, id) VALUES (%s, %s, %s) WHERE NOT EXISTS (SELECT * FROM group_server WHERE id = (%s)"""
        # data = (1085, "silver", 2, 1085)
        #        self.curs.execute(sql2, data)


test_base = DataBase("testah")
