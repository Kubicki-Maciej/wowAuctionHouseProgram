import scraping_site as ss
import apiconnect as apic

class Items:

    def __init__(self):
        self.id_items = 0
        self.list_items = []
        self.list_item_class = []
        self.item_name = ''
        self.url = ''
        self.picture_url = ''
        self.sorted_price_quantity = []
        self.item_name_no_space = ''


    def start(self):
        self.make_url()
        #self.get_name_from_wowhead()

    def make_url(self):
        """ wowhead url """
        self.url = "https://www.wowhead.com/item=" + str(self.id_items)

    def get_name_from_wowhead(self):
        """connect to wowhead to get name items"""
        self.make_url()
        self.item_name = ss.find_name(self.url)
        print(self.item_name)

    def get_information_from_bn(self):
        """

        :return: information from wow api with name
        """
        data = apic.download_item_by_id(self.id_items)
        return data

    def get_name_from_bn(self, default='en_US'):
        data = self.get_information_from_bn()
        self.item_name = data[0]['name'][default] # english name
        self.picture_url = data[1]['assets'][0]['value'] #jpg item

    def check_if_item_is_in_list(self, name_list):
        if self.id_items in name_list:
            print('przedmiot jest tutaj')
            return

    def return_sorted_list_p_q(self):
        return self.sorted_price_quantity

    def create_name_without_space(self):
        item = self.item_name.split()
        self.item_name_no_space = 't'+''.join(item)