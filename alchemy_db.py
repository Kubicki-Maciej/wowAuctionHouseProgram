from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy
from sqlalchemy import Column, Integer, Text, Date, BigInteger, ForeignKey, select, DateTime
from sqlalchemy.dialects.postgresql import JSON
import csv

connection_string = 'postgresql://postgres:war@localhost:5432/sqlalchemy'


def Item_name_base():
    """ insert item name base """

    db = sqlalchemy.create_engine(connection_string)
    engine = db.connect()
    Base = declarative_base()

    class Items_name(Base):
        __tablename__ = "items_name"
        id_item = Column(BigInteger, primary_key=True)
        name = Column(Text)
        url_picture = Column(Text)

    def insert_table_file(session, ins_id, ins_name, ins_url):
        record = Items_name(
            id_item=ins_id,
            name=ins_name,
            url_picture=ins_url
        )
        session.add(record)

    def add_records(file_csv):
        """ create here checker with statement if id item exist in base """
        Base.metadata.create_all(engine)
        SessionFactory = sessionmaker(engine)
        session = SessionFactory()

        with open(file_csv, 'r') as file:
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                try:
                    insert_table_file(session, row[0], row[1], row[2])
                except:
                    print("rekord istnieje")
        session.commit()

    add_records('items.csv')


def File_base(files, dates, server_id):
    """ insert file base not used ?"""
    db = sqlalchemy.create_engine(connection_string)
    engine = db.connect()
    Base = declarative_base()

    class File(Base):
        __tablename__ = 'files'

        name = Column(Text, primary_key=True)
        date = Column(DateTime)
        id_server = Column(Integer)

    def insert_table_file(session, ins_name, ins_date, ins_id_server):
        record = File(
            name=ins_name,
            date=ins_date,
            id_server=ins_id_server
        )
        session.add(record)

    def file_add(files, dates, server_id):
        Base.metadata.create_all(engine)
        SessionFactory = sessionmaker(engine)
        session = SessionFactory()
        for x in range(len(files)):
            insert_table_file(session, files[x], dates[x], server_id)
        session.commit()

    file_add(files, dates, server_id)


def Item_base(date, name, raf, server_id):
    """ insert item base """
    db = sqlalchemy.create_engine(connection_string)
    engine = db.connect()
    Base = declarative_base()

    class File(Base):
        __tablename__ = 'files'

        name = Column(Text, primary_key=True)
        date = Column(DateTime)
        id_server = Column(Integer)

    def insert_table_file(session, ins_name, ins_date, ins_id_server):
        record = File(
            name=ins_name,
            date=ins_date,
            id_server=ins_id_server
        )
        session.add(record)

    def file_add(files, dates, server_id):
        Base.metadata.create_all(engine)
        SessionFactory = sessionmaker(engine)
        session = SessionFactory()

        insert_table_file(session, files, dates, server_id)
        session.commit()

    file_add(name, date, server_id)

    # orm_add(name, name)

    class Item(Base):
        __tablename__ = name

        id = Column(BigInteger, primary_key=True)
        id_item = Column(BigInteger)
        file_name = Column(Text, ForeignKey('files.name'))
        item_name = Column(Text)
        price_b = Column(BigInteger)
        price_u = Column(BigInteger)
        quantity = Column(BigInteger)
        date = Column(DateTime)
        doc = Column(JSON)

    def insert_table_item(session, id_item, f_name, item_name, price_b, price_u, quantity,
                          date_file, json_item, id):
        record = Item(
            id=id,
            id_item=id_item,
            file_name=f_name,
            item_name=item_name,
            price_b=price_b,
            price_u=price_u,
            quantity=quantity,
            date=date_file,
            doc=json_item
        )
        session.add(record)

    def orm_add(file_raf, t_name):
        Base.metadata.create_all(engine)
        SessionFactory = sessionmaker(engine)
        session = SessionFactory()
        id = 1
        for item in file_raf:
            insert_table_item(session, item.id_item, t_name, '',
                              item.price_buyout, item.price_unit, item.quantity,
                              date,
                              item.all_data_item, id)
            id += 1
        session.commit()

    print("dodaje plik " + name + " do bazy danych")

    orm_add(raf, name)


def Items_name():
    db = sqlalchemy.create_engine(connection_string)
    engine = db.connect()
    Base = declarative_base()

    class ItemsName(Base):
        __tablename__ = "items_name"

        id_item = Column(BigInteger, primary_key=True)
        item_name = Column(Text)
        url_picture_item = Column(Text)

    def insert_table_items(session, id_item, item_name, url_picture_item):
        record = ItemsName(
            id_item=id_item,
            item_name=item_name,
            url_picture_item=url_picture_item
        )
        session.add(record)

    def orm_add_model(file_name):
        Base.metadata.create_all(engine)
        SessionFactory = sessionmaker(engine)
        session = SessionFactory()


def check_if_exists_in_files(file_name):
    """
    function need to check if filename exist if not return value
    after that append to db file_name date and server id
    """
    db = sqlalchemy.create_engine(connection_string)
    engine = db.connect()
    Base = declarative_base()

    class File(Base):
        __tablename__ = 'files'
        name = Column(Text, primary_key=True)
        date = Column(DateTime)
        id_server = Column(Integer)

    Base.metadata.create_all(engine)
    SessionFactory = sessionmaker(engine)
    session = SessionFactory()
    # function get by
    stmt = select(File).where(File.name == file_name)
    # stmt = select(File).where(File.name == "ah_103213184_07.16.2021_12;22.json") testing variants

    # if record exist return False if not return True
    with engine.connect() as conn:
        for row in conn.execute(stmt):
            return False
    return True


# w = session.execute(select(File.name, File.id_server). where(File.id_server == 1084)).all()


# select server name in date between
# SELECT name FROM public.files WHERE id_server = 1084
# AND date BETWEEN '2021-07-15' AND '2021-07-30'
