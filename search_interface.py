import database_module as dbm
from psycopg2 import sql

db_name = "sqlalchemy"


class SearchInterface:

    def __init__(self):
        self.db_object = dbm.DataBase(db_name)

    def file_query_by_server_id_and_date(self, server_id, date_range):
        """
        select from files dataframe tables name what we need for get value
        ugly but working got problems with placeholders
        """
        query = "SELECT name, date, id_server FROM files where date > current_date - " + str(date_range) + \
                " AND id_server = " + str(server_id)
        # query = sql.SQL("""
        #         SELECT * FROM files
        #         WHERE
        #         date > current_date -  (%s)
        #         AND
        #         id_server =  (%s)
        #     """),[date_range,server_id]
        return query

    def union_query_join_servers(self, servers, id_item):
        """
        query with represent all items selected by id on server in date range
        """
        select_string = 'SELECT * from "' + servers[0][0] + '" where id_item = ' + str(id_item)
        l_server = len(servers)
        x = 1
        while x < l_server:
            select_string += ' union all SELECT * from "' + servers[x][0] + '" where id_item = ' + str(id_item)
            x += 1
        return select_string

    def union_quert_join_servers_return_values(self, servers, id_item):
        """
        query with sum price , sum quantity , min price , max price , avg item price
        """

        select_string = 'SELECT SUM(price_u) as suma_cen , SUM(quantity) as suma_ilosci , min(price_u) as ' \
                        'minimalna_cena , max(price_u) as maxymalna_cena,' \
                        ' (SUM( price_u * quantity) / SUM(quantity)) as srednia' \
                        ' from "' + servers[0][0] + '" where id_item = ' + str(id_item)
        l_server = len(servers)
        x = 1
        while x < l_server:
            select_string += 'union all SELECT SUM(price_u) as suma_cen , SUM(quantity) as suma_ilosci , min(price_u) '\
                             'as minimalna_cena , max(price_u) as maxymalna_cena' \
                             ', (SUM( price_u * quantity) / SUM(quantity)) as srednia' \
                             ' from "' + servers[x][0] + '" where id_item = ' + str(id_item)
            x += 1
        return select_string

    def get_name_from_table(self, id_item):
        query = 'SELECT name FROM items_name WHERE id_item = %s'
        data_list = [id_item, ]
        name = self.db_object.execute_query_with_arg(query, data_list)
        return name[0][0]

    def test_def(self, id_item, id_server, search_range):
        name = self.get_name_from_table(id_item)
        # Anchor Weed

        files_query = self.file_query_by_server_id_and_date(id_server, search_range)
        # should query get servers table name

        records_files = self.db_object.execute_query(files_query)
        # should get records with table name

        items_query = self.union_query_join_servers(records_files, id_item)
        # should get query with tables name, union and search by id

        test = self.union_quert_join_servers_return_values(records_files, id_item)

        items_records = self.db_object.execute_query(items_query)
        # should get items records

        return name, files_query, records_files, items_query, items_records, test


objectSearch = SearchInterface()

s = objectSearch.test_def(152510, 1084, 30)
