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
                        'login': 'quest',
                        'password': None
                    }],
                    'history': []
                }
                json.dump(self.data, fo)

    def get_user(self, username):
        for user in self.data['users']:
            if username == user['login']:
                return user
        return None

    def check_password(self,password,user):
        if password == user['password']:
            return True
        return False

    def get_id_last_oper(self):
        return len(self.data['history'])+1

    def add_operation(self,oper,username):
        if username == 'quest':
            pass
        else:
            new_oper = {
                    'id': self.get_id_last_oper(),
                    'login': username,
                    'time': datetime.today().strftime("%d-%m-%Y"),
                    'operation': oper
                }
            self.data['history'].append(new_oper)
            self.write_data()

    def get_history(self,username,all):
        if all:
            return [oper for oper in self.data['history'] if oper['login'] == username]
        return [oper for oper in self.data['history']
                if oper['login'] == username and
                datetime.today().date() == datetime.strptime(oper['time'],"%d-%m-%Y").date()]

    #Made anton change Mykola:)
    def check_pass(self,pass1, pass2):
        if pass1 != pass2:
            print('pass1 != pass2')
            return False
        elif len(pass1) < 8:
            print('len(pass1) < 8')
            return False
        return True

    def register(self,login):
        repeat_register = True
        user = None
        while repeat_register:
            try:
                print('-' * 40)
                print('login >>> {}'.format(login))
                password = input('paswword (8+ symbol)>>> ').strip()
                confirm_password = input('repeat password>>> ').strip()
                if self.check_pass(password, confirm_password):
                    try:
                        user = self.write_user(login=login, password=password)
                        repeat_register = False
                        print('register success!')
                    except ValueError as e:
                        repeat_register = True
                        print(e)
                else:
                    print('incorrect password')
            except Exception as e:
                print(e)
        return user

    def write_user(self,**new_user):
        new_id = len(self.data['users'])
        new_user.update({
            'id': new_id
        })
        self.data['users'].append(new_user)
        self.write_data()
        return new_user['login']
