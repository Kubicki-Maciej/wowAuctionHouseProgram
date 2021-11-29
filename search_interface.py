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

    def order_by_query_join_servers(self, servers, id_item):
        """
        query with represent all items selected by id on server in date range
        """
        x = 1
        select_string = 'SELECT * from "' + servers[0][0] + '" where id_item = ' + str(id_item)
        l_server = len(servers)

        while x < l_server:
            select_string += ' union all SELECT * from "' + servers[x][0] + '" where id_item = ' + str(id_item)
            x += 1
        select_string += " Order By Date"
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
            select_string += 'union all SELECT SUM(price_u) as suma_cen , SUM(quantity) as suma_ilosci , min(price_u) ' \
                             'as minimalna_cena , max(price_u) as maxymalna_cena' \
                             ', (SUM( price_u * quantity) / SUM(quantity)) as srednia' \
                             ' from "' + servers[x][0] + '" where id_item = ' + str(id_item)
            x += 1
        return select_string

    def union_query_with_date_order_join_servers_return_values(self, servers, id_item):
        """
        query with sum price , sum quantity , min price , max price , avg item price
        """

        select_string = 'SELECT date, SUM(price_u) as suma_cen , SUM(quantity) as suma_ilosci , min(price_u) as ' \
                        'minimalna_cena , max(price_u) as maxymalna_cena,' \
                        ' (SUM( price_u * quantity) / SUM(quantity)) as srednia ' \
                        ' from "' + servers[0][0] + '" where id_item = ' + str(id_item) + ' group by date'
        l_server = len(servers)
        x = 1
        while x < l_server:
            select_string += ' union all SELECT date, SUM(price_u) as suma_cen , SUM(quantity) as suma_ilosci , ' \
                             'min(price_u) ' \
                             'as minimalna_cena , max(price_u) as maxymalna_cena' \
                             ', (SUM( price_u * quantity) / SUM(quantity)) as srednia' \
                             ' from "' + servers[x][0] + '" where id_item = ' + str(id_item) + ' group by date'
            x += 1
        select_string += " order by date"
        return select_string

    def get_name_from_table(self, id_item):
        query = 'SELECT name FROM items_name WHERE id_item = %s'
        data_list = [id_item, ]
        name = self.db_object.execute_query_with_arg(query, data_list)
        return name[0][0]

    def get_by_single_query_data(self, server, id_item):

        select_string = 'SELECT date, SUM(price_u) as suma_cen , SUM(quantity) as suma_ilosci , min(price_u) as ' \
                        'minimalna_cena , max(price_u) as maxymalna_cena,' \
                        ' (SUM( price_u * quantity) / SUM(quantity)) as srednia, ' \
                        ' from "' + server + '" where id_item = ' + str(id_item) + ' group by date'
        return select_string

    def multiple_servers_by_one_query(self, servers, id_item):
        list_multiple_servers = []
        for server in servers:
            list_multiple_servers.append(self.get_by_single_query_data(server[0], id_item))
        return list_multiple_servers

    def get_info_needed_to_table(self, id_item, id_server, search_range):
        """  function needed to make tables in data_representation
        return:
           (date, sum price, sum quantity, min price, max price, avg price) AND ORDER BY DATE
        """
        files_query = self.file_query_by_server_id_and_date(id_server, search_range)

        records_files = self.db_object.execute_query(files_query)

        query = self.union_query_with_date_order_join_servers_return_values(records_files, id_item)

        average_query_by_order = self.db_object.execute_query(query)

        # files_query = self.file_query_by_server_id_and_date(id_server, search_range)
        # records_files = self.db_object.execute_query(files_query)
        # sort_order = self.order_by_query_join_servers(records_files, id_item)
        # items_records_by_sort_order = self.db_object.execute_query(sort_order)


        return average_query_by_order

    def test_def(self, id_item, id_server, search_range):
        """
        data: tuple
            data[0]: Item name
            data[1]: Query asking files to get file (tables name)
            data[2]: Output from query data[1]
            data[3]: Query with union asking to get item by id
            data[4]: Output form query data[3]
            data[5]: Query that sum price, sum quantity, min price, max price, avg price
            data[6]: Output form query data[5]:
                sum price[0], sum quantity[1], min price[2], max price[3], avg price[4]3
            data[7]: Query get all items and ORDER BY DATE
            data[8]: Output form query data[7]:
            data[9]: Query that return
                (date, sum price, sum quantity, min price, max price, avg price) AND ORDER BY DATE
            data[10]: Output form query data[9]
            data[11]: Multiple query servers
            data[12]: data in one function return
                (date, sum price, sum quantity, min price, max price, avg price) AND ORDER BY DATE
        """
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

        avrage_query = self.db_object.execute_query(test)

        # added new function problem with union, dosen't work as intended
        sort_order = self.order_by_query_join_servers(records_files, id_item)
        # query string with order by

        items_records_by_sort_order = self.db_object.execute_query(sort_order)
        # data from sort order

        query_sum_2 = self.union_query_with_date_order_join_servers_return_values(records_files, id_item)

        avrage_query_by_order = self.db_object.execute_query(query_sum_2)

        multiple_query_servers_by_one = self.multiple_servers_by_one_query(records_files, id_item)

        info_from_table = self.get_info_needed_to_table(id_item, id_server, search_range)

        return name, files_query, records_files, items_query, items_records, test, avrage_query, sort_order, \
               items_records_by_sort_order, query_sum_2, avrage_query_by_order, multiple_query_servers_by_one, info_from_table


objectSearch = SearchInterface()
#
# s = objectSearch.test_def(152510, 1084, 60)


#  data needed to make charts
g = objectSearch.get_info_needed_to_table(152510, 1084, 60)
