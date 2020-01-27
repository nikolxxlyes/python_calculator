import json
from datetime import datetime

class CalcHistory:
    def __init__(self):
        """загрузка файла истории или создание его"""
        self.file_name = 'calc_history.json'
        self.data = ''
        try:
            with open(self.file_name) as self.fo:
                self.data = json.load(self.fo)

        except FileNotFoundError:
            self.write_data()

    def write_data(self):
        with open(self.file_name, 'w') as fo:
            if not self.data:
                self.data = {
                    'users': [{
                        'username': 'quest',
                        'password': None
                    }],
                    'history': [{
                        'id': 0,
                        'username': 'quest',
                        'time': datetime.today().strftime("%d-%m-%Y"),
                        'operation': None
                    }]
                }
            json.dump(self.data, fo)

    def is_user(self, username):
        for user in self.data['users']:
            if username == user['username']:
                return user
        return None

    def reg_user(self,username,password):
        new_user ={
            'username': username,
            'password': password
        }
        self.data['users'].append(new_user)
        self.write_data()

    def check_password(self,password,user):
        if password == user['password']:
            return True
        return False

    def get_id_last_oper(self):
        return len(self.data['history'])

    def add_operation(self,oper,username):
        new_oper = {
                    'id': self.get_id_last_oper(),
                    'username': username,
                    'time': datetime.today().strftime("%d-%m-%Y"),
                    'operation': oper
                }
        self.data['history'].append(new_oper)
        self.write_data()

    def get_history(self,username,all):
        if all:
            return [oper for oper in self.data['history'] if oper['username'] == username]
        else:
            return [oper for oper in self.data['history']
                    if oper['username'] == username and
                    datetime.today().date() == datetime.strptime('27-01-2020',"%d-%m-%Y").date()]