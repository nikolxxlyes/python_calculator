import json
from datetime import datetime

class CalcHistory:
    def __init__(self):
        """загрузка файла истории или создание его"""
        self.file_name = 'calc_history.json'
        try:
            with open(self.file_name) as self.fo:
                self.data = json.load(self.fo)

        except FileNotFoundError:
            self.write_data()

    def write_data(self):
        with open(self.file_name, 'w') as fo:
            try:
                json.dump(self.data, fo)
            except AttributeError:
                self.data = {
                    'users': [{
                        'id': 0,
                        'username': 'quest',
                        'password': None
                    }],
                    'history': []
                }
                json.dump(self.data, fo)

    def get_user(self, username):
        for user in self.data['users']:
            if username == user['username']:
                return user
        return None

    def reg_user(self,username,password):
        new_user ={
            'id': self.get_id_last_user(),
            'username': username,
            'password': password
        }
        self.data['users'].append(new_user)
        self.write_data()

    def check_password(self,password,user):
        if password == user['password']:
            return True
        return False

    def get_id_last_user(self):
        return len(self.data['users'])

    def get_id_last_oper(self):
        return len(self.data['history'])+1

    def add_operation(self,oper,username):
        if username == 'quest':
            pass
        else:
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
        return [oper for oper in self.data['history']
                if oper['username'] == username and
                datetime.today().date() == datetime.strptime(oper['time'],"%d-%m-%Y").date()]