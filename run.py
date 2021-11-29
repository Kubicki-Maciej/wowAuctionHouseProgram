import sys
from PyInquirer import prompt
import os

""" that represent manager of WoW programs """


def ask_program():
    options = {
        'type': 'list',
        'name': 'choice',
        'message': 'What you want to run?',
        'choices': [
            '1.Run auction house program',
            '2 Run Json download program',
            '3 Add ah data from x server to database PG',
            '4 Check if new items exist',
            '5 Exit'
        ]
    }
    return prompt(options)['choice']


def ask_with_json_download():
    options = {
        'type': 'list',
        'name': 'choice',
        'message': 'What you want to run?',
        'choices': [
            # '1.Run Gui Program',
            '1 Get from Id server json file',
            '2 Get from Name server json file',
            '3 Downloads all servers',
            '4 Return back'
        ]
    }
    return prompt(options)['choice']


def ask_with_files_add_to_db():
    options = {
        'type': 'list',
        'name': 'choice',
        'message': 'What you want to run?',
        'choices': [
            '1.Add to DataBase by id',
            '2 Add to DataBase by name',
            '3 Add all files to Data Base',
            '4 Return back'
        ]
    }
    return prompt(options)['choice']


def run_ah_program():
    import main
    print('starting ah program')


def check_server_by_id(text_input):
    import realmlist
    x = realmlist.check_if_id_exist(int(text_input))
    print(x)
    return x


def inject_all_data_to_db():
    import realmlist
    import db_program
    for server in realmlist.list_id_server:
        db_program.add_to_db_files_from_container(server)


def check_server_by_name(text_input):
    import realmlist
    id = realmlist.function_returning_id_of_lookin_server_by_name(text_input)
    return id

def update_item_base():
    import data_save
    data_save.run_data_save()

def run_json_program():
    platform = ask_with_json_download()

    # if '1' in platform:
    #     #  with gui or not? with input or all files in data ?
    #     import wow_server_manager.main

    if '1' in platform:
        ques = {
            'type': 'input',
            'name': 'id',
            'message': 'Enter id server that should be downloaded:'
        }
        input_from = prompt(ques)['id']

        if check_server_by_id(input_from):
            import downloadFile
            downloadFile.downloadFunction(input_from)
        else:
            print('wrong id')
        run_json_program()

    elif '2' in platform:
        ques = {
            'type': 'input',
            'name': 'name',
            'message': 'Enter name server that should be downloaded:'
        }
        import realmlist
        # check if name is in json file connected realm if not return false
        input_from = prompt(ques)['name']
        id_server = realmlist.function_returning_id_of_lookin_server_by_name(input_from)

        if id_server:
            import downloadFile
            downloadFile.downloadFunction(id_server)
        run_json_program()

    elif '3' in platform:
        import downloadFile
        downloadFile.download_all_servers()
        run_json_program()

    elif '4' in platform:
        main()


def run_db_program():
    """
     '1.Add to DataBase by id',
            '2 Add to DataBase by name',
            '3 Add all files to Data Base',
            '4 Return back'
    """

    platform = ask_with_files_add_to_db()

    if '1' in platform:
        ques = {
            'type': 'input',
            'name': 'name',
            'message': 'Enter id server that should be downloaded:'
        }
        text_input = prompt(ques)['name']
        if check_server_by_id(text_input):
            import db_program
            db_program.add_to_db_files_from_container(int(text_input))
            print('done')
        else:
            print('wrong id')

        run_db_program()

    elif '2' in platform:
        ques = {
            'type': 'input',
            'name': 'name',
            'message': 'Enter name server that should be downloaded:'
        }
        import realmlist
        # check if name is in json file connected realm if not return false
        text_input = prompt(ques)['name']
        id_server = realmlist.function_returning_id_of_lookin_server_by_name(text_input)
        if id_server:
            import db_program
            db_program.add_to_db_files_from_container(int(id_server))
        run_db_program()

    elif '3' in platform:
        inject_all_data_to_db()
        run_db_program()
    elif '4' in platform:
        main()


def main():
    platform = ask_program()

    if '1' in platform:
        run_ah_program()
    elif '2' in platform:
        run_json_program()
    elif '3' in platform:
        run_db_program()
    elif '4' in platform:
        print('working')
        update_item_base()
    elif '5' in platform:
        sys.exit()

    threads = []


if __name__ == "__main__":
    main()
