from calc.data import CalcHistory
from calc.function import get_user,get_data_oper,calculator

def calc():
    more_option = True if username != 'quest' else False
    print(f'{username}, lets calculate !!!')
    while True:
        args = get_data_oper(more_option)
        try:
            oper = calculator(*args, more_option=more_option)
            if isinstance(oper,str):
                print(oper)
            elif username == 'quest':
                print(oper[0])
            else:
                print(oper[0])
                history.add_operation(oper[0], username)
        except TypeError:
            print('Incorrect data.')
        more_calc = input("Once again? (y/n) >>> ")
        if more_calc == 'n':
            break

def show_history():
    if username == 'quest':
        print("Quest don't have history. This option for registered user!")
    else:
        part_history = input("All history? (y/n) >>>")
        if part_history == 'y':
            all = 'yes'
        else:
            all = ''
        user_history = history.get_history(username, all)
        print(f'{username} have operation: {len(user_history)}')
        for i, oper in enumerate(user_history):
            print(f"{i + 1}. {oper['operation']} / {oper['time']}")

def change_user():
    change = input('Change user? (y/n) >>> ')
    if change == 'y':
        global username
        username = get_user(history)
    # return username

def main_menu():
    cont = True
    while cont:
        print('-'*40)
        print("1. Calculator\n2. Show history\n3. Change user\n4. Quit")
        request = input('>>> ')
        if request == "1":
            calc()
        elif request == '2':
            show_history()
        elif request == "3":
            change_user()
        elif request == "4":
            cont = False
        else:
            print("Incorrect request. Try again")

def main():
    global history, username
    history = CalcHistory()
    print("Hello, quest!")
    username = get_user(history)
    main_menu()

main()