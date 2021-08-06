import comparison as com
from realmlist import list_id_server

"""
class used to get information from class Comparison
stores all data probably not best option load all files
"""


class Connector:

    def __init__(self):
        self.objects_Comparison = []
        self.objects_id = []

    def get_comparison_obj_to_list(self, list_id, time_interval):

        for id_number in list_id:

            temp_obj = com.Comparison()
            temp_obj.create_dependency_of_ahfile()
            temp_obj.runFileChoice()
            # make_objects_add_them_to_file when first variable is 0 - 2 represent day,week,month
            temp_obj.make_objects_add_them_to_file(time_interval, id_number)
            if temp_obj.list_of_raf_file:
                temp_obj.runFileChoice()
                self.objects_Comparison.append(temp_obj)
            else:
                print(str(id_number) + " nie ma pliku json o tym id")

    def get_file_names(self, object_comparison):
        temp_list = []
        for t in object_comparison.info_about_item:
            temp_list.append(t[3])
        return temp_list

    def get_file_date(self, object_comparison):
        temp_list = []
        for t in object_comparison.info_about_item:
            temp_list.append(t[0][2])
        return temp_list

    def for_many_objects(self):
        """
        that runs for all objects comparison,
        get from them file_names with same id and dates
        then return in tuple [0]
        """
        temp_list_date = []
        temp_list_name = []
        for obj in self.objects_Comparison:
            temp_list_date.append(self.get_file_date(obj))
            temp_list_name.append(self.get_file_names(obj))

        return temp_list_date, temp_list_name

lista = [1084]
t = Connector()
t.get_comparison_obj_to_list(lista, 2)
