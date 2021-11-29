# test second variation each item has its own table.


import database_module as dbm

import time
# db_test_1 = dbm.DataBase("wowDB")
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy
from sqlalchemy import Column, Integer, Table, Text, Date, BigInteger, ForeignKey, select, DateTime, MetaData, String
from sqlalchemy.dialects.postgresql import JSON
from db_program import t



class DataBaseItemOwnTable:
    def __init__(self, table_name, date, id, list_m):
        self.connect_string = 'postgresql://postgres:war@localhost:5432/owntable'
        self.db = sqlalchemy.create_engine(self.connect_string)
        self.engine = self.db.connect()
        self.table_name = table_name
        self.date = date
        self.id = id
        self.list_items = list_m
        self.meta = MetaData()

        self.Base = declarative_base()

        class Files(self.Base):
            __tablename__ = 'files'
            __table_args__ = {'extend_existing': True}
            # id = Column(BigInteger, primary_key=True, autoincrement=True)
            name = Column(Text, primary_key=True)
            date = Column(DateTime)
            id_server = Column(Integer)

        def insert_table_file(session, ins_name, ins_date, ins_id_server):
            record = Files(
                name=ins_name,
                date=ins_date,
                id_server=ins_id_server
            )
            session.add(record)

        def file_add(files, dates, server_id):
            self.Base.metadata.create_all(self.engine)
            SessionFactory = sessionmaker(self.engine)
            session = SessionFactory()

            insert_table_file(session, files, dates, server_id)
            session.commit()

        file_add(self.table_name, self.date, self.id)

        # represent of single item class
        def single_item_add(table_id, item_list, t_name, session):

            class Items_name(self.Base):
                __tablename__ = table_id

                id = Column('id', Integer, primary_key=True, autoincrement=True)
                id_item = Column(BigInteger)
                file_name = Column(Text)
                item_name = Column(Text)
                price_b = Column(BigInteger)
                price_u = Column(BigInteger)
                quantity = Column(BigInteger)
                doc = Column(JSON)

            def insert_table_item(session, id_item, f_name, item_name, price_b, price_u, quantity,
                                  json_item, ):
                record = Items_name(

                    id_item=id_item,
                    file_name=f_name,
                    item_name=item_name,
                    price_b=price_b,
                    price_u=price_u,
                    quantity=quantity,
                    doc=json_item
                )
                session.add(record)

            def orm_add(single_items, tablename):
                for item in single_items:
                    insert_table_item(session, item.id_item, tablename, '',
                                      item.price_buyout, item.price_unit, item.quantity,
                                      item.all_data_item)

            orm_add(item_list, t_name)

        def multi_items_add(items_list, t_name):
            self.Base.metadata.create_all(self.engine)
            SessionFactory = sessionmaker(self.engine)
            session = SessionFactory()
            counter = 0
            session_counter = 1
            for item in items_list:
                counter += 1
                table_id = "table" + str(item.id_items)
                try:
                    single_item_add(table_id, item.list_item_class, t_name, session)
                except:
                    print(counter)
                    print("problem with " + table_id)
                if counter % 500 == 0:
                    print("session commit" + str(session_counter))
                    session_counter += 1
                    session.commit()

            #     problem with commit on session
            session.commit()

        # print(self.table_name)
        # multi_items_add(self.list_items, self.table_name)

    # new not orm adding
    """ second part of code trying to make """

    def get_item_table_str(self, id_item):
        tb_name = "item" + str(id_item)
        return tb_name

    def item_table_structure(self, id_item):

        item_name = self.get_item_table_str(id_item)
        item = Table(
            item_name, self.meta,
            Column('id', Integer, primary_key=True, autoincrement=True),
            Column('id_item', BigInteger),
            Column('file_name', Text),  # add here FG
            Column('item_name', Text),
            Column('price_b', BigInteger),
            Column('price_u', BigInteger),
            Column('quantity', BigInteger),
            Column('doc', JSON),
            extend_existing=True,
        )
        return item

    def create_table(self, id_item):
        self.item_table_structure(id_item)
        self.meta.create_all(self.engine)

    def dict_maker_item(self, obj_item):

        list_dict = []
        for item in obj_item.list_item_class:
            temp_dict = {
                'id_item': item.id_item,
                'file_name': self.table_name,
                'item_name': "",
                'price_b': item.price_buyout,
                'price_u:': item.price_unit,
                'quantity': item.quantity,
                'doc': item.all_data_item
            }
            list_dict.append(temp_dict)

        return list_dict

    # function used to test

    def values_str_by_list_item_class(self, object_item):

        table_name = self.table_name
        id_item = object_item.id_item
        item_name = ""
        price_buyout = object_item.price_buyout
        price_unit = object_item.price_unit
        quantity = object_item.quantity
        json = object_item.all_data_item
        single_value = "(" + str(id_item) + ", " + table_name + ", " + item_name + ", " + str(price_buyout) + ", " + \
                       str(price_unit) + ", " + str(quantity) + ", " + str(json) + ")"
        return single_value

    def create_values_for_single_table(self, object_items):

        list_of_single_value = []
        for object_item in object_items:
            list_of_single_value.append(self.values_str_by_list_item_class(object_item))
        converted_values = ", ".join(list_of_single_value)
        return converted_values

    def create_query_for_single_table(self, items):



        records_to_add = self.create_values_for_single_table(items.list_item_class)
        id_item = items.id_items
        name = self.get_item_table_str(id_item)
        insert_single_item = " insert into " + name + " values " + records_to_add + ";"
        create_table = "CREATE TABLE IF NOT EXISTS "+name + "(id_item Int, file_name Text, item_name Text, price_b  " \
                                                            "Bigint, price_u Bigint, quantity BigInt, doc Text ); "
        return insert_single_item, create_table

    def create_query_for_all_tables(self):
        tic = time.perf_counter()
        big_list = []
        big_table_list = []
        for items in self.list_items:
            tuple_func = self.create_query_for_single_table(items)
            big_list.append(tuple_func[0])
            big_table_list.append(tuple_func[1])
        big_query = ' '.join(big_list)
        big_table_query = ' '.join(big_table_list)
        toc = time.perf_counter()
        print(f" dodawanie do bazy trwało: {toc - tic:0.4f} seconds")
        return big_query, big_table_query



    def list_maker(self, id_item):
        """ test dict maker"""
        list_dict = []
        for x in range(5):
            e = {'id_item': id_item,
                 'file_name': "test",
                 'item_name': "test",
                 'price_b': 2,
                 'price_u:': 1,
                 'quantity': x,
                 'doc': {'id': 1812908588, 'item': {'id': 25, 'context': 75}, 'buyout': 3452120100,
                         'quantity': 1, 'time_left': 'LONG'}}
            list_dict.append(e)
        return list_dict

    def execute_con(self, id_item, object_item):
        # https: // www.tutorialspoint.com / sqlalchemy / sqlalchemy_core_executing_expression.htm
        """ execute single table"""
        ins_list = self.dict_maker_item(object_item)

        table_structure = self.item_table_structure(id_item)
        self.engine.execute(table_structure.insert(), ins_list)

    def add_all_items(self):
        # counter = 0
        for item in self.list_items:
            self.create_table(item.id_items)
            self.execute_con(item.id_items, item)

            # counter += 1
            # if counter == 25:
            #     break


list_obj = []

count_items = len(t[0])
# for x in range(count_items):
tic = time.perf_counter()
list_obj.append(DataBaseItemOwnTable(t[1][0], t[2][0], t[3], t[0][0]))
toc = time.perf_counter()

w = list_obj[0]
qw = w.create_query_for_all_tables()

tic = time.perf_counter()
# w.add_all_items()
toc = time.perf_counter()
print(f" dodawanie do bazy trwało: {toc - tic:0.4f} seconds")

""" tworzenie bazy i laczenie sie do niej"""

recordss = qw[0]
tables = qw[1]

db = dbm.DataBase("owntable")
db.execute_insert_query(tables)
db.execute_insert_query(recordss)



# stworz_tabele(35)
# insertuj_table(35)


# w.execute_con(45)
# w.create_table(455)
# w.execute_con(455)
# a = [SQL: INSERT INTO table2594 (id_item, file_name, item_name, price_b, price_u, quantity, doc) VALUES (%(
# id_item)s, %(file_name)s, %(item_name)s, %(price_b)s, %(price_u)s, %(quantity)s, %(doc)s) RETURNING table2594.id]
# b
# = [parameters: {'id_item': 2594, 'file_name': 'ah_1084_07.10.2021_17;27.json', 'item_name': '', 'price_b': 0,
# 'price_u': 1062100, 'quantity': 1, 'doc': '{"id": 1812838610, "item": {"id": 2594}, "quantity": 1, "unit_price":
# 1062100, "time_left": "LONG"}'}]
