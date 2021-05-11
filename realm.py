

class Realm:
    """
    clas represent a server,
    contain: name_of_realm, ah_json , active, id_server, group_server(true/false), url, population
    functions:
    """

    def __init__(self,):

        self.realm_id = 0
        self.name_of_realm = ''
        self.ah_json_path = ''
        self.id_server = 0
        self.group_server = []
        self.url = ''
        self.population = ''