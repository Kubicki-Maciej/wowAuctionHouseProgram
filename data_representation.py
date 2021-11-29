from search_interface import objectSearch
import pandas as pd
import plotly.express as px

def get_data_and_process_it(data):
    """
    from search_interface test_def
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
         data[11]: Multiple servers by one
    """

    item_name = data[0]
    # save_data_to_log(data)
    data_list = []
    avg_list = []
    for x in range(len(data)):
        data_list.append(data[x][0])
        # we divining by 10000 to get gold price
        avg_list.append(data[x][5]/10000)

    return item_name, data_list, avg_list


# def dont_working_get_data_and_process_it(data):
#     # don't working right function problem with union all
#
#     """
#     from search_interface test_def
#     data: tuple
#          data[0]: Item name
#          data[1]: Query asking files to get file (tables name)
#          data[2]: Output from query data[1]
#          data[3]: Query with union asking to get item by id
#          data[4]: Output form query data[3]
#          data[5]: Query that sum price, sum quantity, min price, max price, avg price
#          data[6]: Output form query data[5]:
#              sum price[0], sum quantity[1], min price[2], max price[3], avg price[4]3
#          data[7]: Query get all items and ORDER BY DATE
#          data[8]: Output form query data[7]:
#          data[9]: Query that return
#          (date, sum price, sum quantity, min price, max price, avg price) AND ORDER BY DATE
#          data[10]: Output form query data[9]
#     """
#
#     item_name = data[0]
#     save_data_to_log(data)
#     data_list = []
#     avg_list = []
#     for x in range(len(data[2])):
#         data_list.append(data[2][x][1])
#         avg_list.append(data[6][x][4])
#
#     return item_name, data_list, avg_list

def save_data_to_log(data):
    """ created data to test problem with showing chart"""

    import logging

    Log_Format = "%(levelname)s %(asctime)s - %(message)s"

    logging.basicConfig(filename="logfile.log",
                        filemode="a",
                        format=Log_Format,
                        level=logging.DEBUG)

    logger = logging.getLogger()

    logger.error("Our First Log Message")

    print = logger.info

    print("------------------")
    print("data[1]: Query asking files to get file (tables name)")
    print("------------------")
    print(data[1])
    print("------------------")
    print("data[2]: Output from query data[1]")
    print("------------------")
    print(data[2])
    print("------------------")
    print("data[3]:Query with union asking to get item by id")
    print("------------------")
    print(data[3])
    print("------------------")
    print("data[4]:Output form query data[3]")
    print("------------------")
    print(data[4])
    print("------------------")
    print("data[5]: Query that sum price, sum quantity, min price, max price, avg price")
    print("------------------")
    print(data[5])
    print("------------------")
    print("data[6]:Output form query data[5]: sum price[0], sum quantity[1], min price[2], max price[3], avg price[4]")
    print("------------------")
    print(data[6])
    print("------------------")
    print("data[7]: Query get all items and ORDER BY DATE")
    print("------------------")
    print(data[7])
    print("------------------")
    print("data[8]: Output form query data[7]:")
    print("------------------")
    print(data[8])
    print("------------------")
    print("data[9]: Query that return (date, sum price, sum quantity, min price, max price, avg price) AND ORDER BY DATE")
    print("------------------")
    print(data[9])
    print("------------------")
    print("data[10]: Output form query data[9]")
    print("------------------")
    print(data[10])
    print("------------------")


def web_page_data(id_item, id_server, server_range=30):

    data = objectSearch.get_info_needed_to_table(id_item, id_server, server_range)
    item_name = objectSearch.get_name_from_table(id_item)

    procesed_data = get_data_and_process_it(data)

    table_obj = pd.Series(procesed_data[2], index=procesed_data[1])

    dat = pd.DataFrame({
        item_name: procesed_data[1],
        'avg': procesed_data[2],
    }, columns=[item_name, 'avg'])

    # top_followers = df.sort_values(by='followers', axis=0, ascending=False)[:100]

    fig = px.bar(dat,
                 x=item_name,
                 y='avg',
                 )
    fig.show()

def testrun():

    data = objectSearch.get_info_needed_to_table(152510, 1084, 30)
    item_name = objectSearch.get_name_from_table(152510)

    procesed_data = get_data_and_process_it(data)

    table_obj = pd.Series(procesed_data[2], index=procesed_data[1])

    dat = pd.DataFrame({
        item_name: procesed_data[1],
        'avg': procesed_data[2],
    }, columns=[item_name, 'avg'])

    # top_followers = df.sort_values(by='followers', axis=0, ascending=False)[:100]

    fig = px.bar(dat,
                 x=item_name,
                 y='avg',
                 )
    fig.show()


# w = get_data_and_process_it(s)
#
# data = pd.Series(w[2], index=w[1])
#
#
# dat = pd.DataFrame({
#     'data': w[1],
#     'avg': w[2],
# }, columns=['data','avg'])
#
#
# # top_followers = df.sort_values(by='followers', axis=0, ascending=False)[:100]
#
# fig = px.bar(dat,
#              x='data',
#              y='avg',
#             )
#
# fig.show()