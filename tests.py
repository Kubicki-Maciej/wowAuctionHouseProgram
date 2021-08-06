# test second variation each item has its own table.

import database_module as dbm

import time
# db_test_1 = dbm.DataBase("wowDB")
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy
from sqlalchemy import Column, Integer, Text, Date, BigInteger, ForeignKey, select, DateTime
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

        self.Base = declarative_base()

        class Files(self.Base):
            __tablename__ = 'files'
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

        def single_item_add(table_id, item_list, t_name, session):

            class Items_name(self.Base):

                __tablename__ = table_id
                id = Column('id', Integer,  primary_key=True, autoincrement=True)
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
            for item in items_list:
                table_id = "table" + str(item.id_items)
                single_item_add(table_id, item.list_item_class, t_name, session)
            #     problem with commit on session
            session.commit()

        print(self.table_name)
        multi_items_add(self.list_items, self.table_name)

list_obj = []
count_items = len(t[0])
# for x in range(count_items):
tic = time.perf_counter()
list_obj.append(DataBaseItemOwnTable(t[1][0], t[2][0], t[3], t[0][0]))
toc = time.perf_counter()
print(f" dodawanie do bazy trwało: {toc - tic:0.4f} seconds")
