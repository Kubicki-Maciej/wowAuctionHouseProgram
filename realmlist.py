import json
import realm as r
import server_group as sg

list_class_realm = []
list_class_server = []
list_id_server = []


def open_file(file_name):
    """open file"""

    opened_file = open(file_name, "r", encoding="utf-8")
    return opened_file


def open_json_file(file_name):
    """open imported from blizzard json file with realms"""

    file = open_file(file_name)
    data = json.load(file)
    # new_data = json.dumps(data, indent=2)
    return data


path = 'connected-realm.json'
data = open_json_file(path)


def create_class_realms(data):
    """
    the function uses objects from class: server_group.ServerGroup and realm.Realm
    empty_realms represent group of servers, contain uniqe id for the group of servers imported from
    json file connected-realm.json. 
    aslo second (for) loop extract single server with uniqe name.
    """
    # create json file to save represent of class  ?? if it not exist activate this create_class_realms and save it

    for empty_realms in data['results']:

        id = empty_realms['data']['id']
        realms_list = empty_realms['data']['realms']
        href_key = empty_realms['key']['href']

        _realms = sg.ServerGroup()

        _realms.id_group = id
        _realms.list_of_server = realms_list
        _realms.href_key = href_key

        list_class_server.append(_realms)

        to_realm = empty_realms['data']
        for realm in to_realm['realms']:
            name = realm['name']['en_GB']
            realm_id = realm['id']

            realm = r.Realm()

            realm.group_server = _realms
            realm.id_server = id
            realm.ah_json = _realms.ah_json_path
            realm.name_of_realm = name
            realm.realm_id = realm_id

            list_class_realm.append(realm)


def function_returning_id_of_lookin_server_by_name(name_of_server):
    for x in list_class_realm:

        if x.name_of_realm == name_of_server:
            id_server = x.id_server
            return id_server


def find_from_name(name, list_class_servers):
    for servers in list_class_servers:

        for server in servers.list_of_server:
            if server['name']['en_GB'] == name:
                print(server)
                print(servers.id_group)
                temp_list = servers.list_of_server
                for serv_name in temp_list:
                    print(serv_name['name']['en_GB'])

                return servers.id_group, temp_list


def check_if_id_exist(id_server):
    for element in list_id_server:
        if id_server == element:
            return True

def function_returning_id_of_lookin_server_by_name(name_of_server):

    for x in list_class_realm:

        if x.name_of_realm == name_of_server:
            id_server = x.id_server
            return id_server
    print('wrong name')
    return False




def get_id_list(list_class_server):

    for server in list_class_server:
        list_id_server.append(server.id_group)


create_class_realms(data)
get_id_list(list_class_server)
# g = find_from_name("Tarren Mill", list_class_server)