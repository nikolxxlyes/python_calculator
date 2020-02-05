from calc.data import CalcHistory
from calc.function import get_user,get_data_oper,calculator

def calc(history, username):
    more_option = True if username != 'quest' else False
    print(f'{username}, lets calculate !!!')
    while True:
        try:
            oper = calculator(more_option)
            print(oper)
            history.add_operation(oper, username)
        except TypeError:
            print('Incorrect data.')
        except KeyError as key:
            print(f"{key} isn't supported operation")
        except ZeroDivisionError:
            print("Division by is invalid operation")
        except Exception as e:
            print(0)
            print(type(e), e)
        more_calc = input("Once again? (y/n) >>> ")
        if more_calc == 'n':
            break

def show_history(history, username):
    if username == 'quest':
        print("Quest don't have history. This option for registered user!")
    else:
        part_history = input("All history? (y/n) >>>").strip()
        if part_history == 'y':
            all = 'yes'
        else:
            all = ''
        user_history = history.get_history(username, all)
        print(f'{username} have operation: {len(user_history)}')
        for i, oper in enumerate(user_history):
            print(f"{i + 1}. {oper['operation']} / {oper['time']}")

def change_user(history, username):
    change = input('Change user? (y/n) >>> ').strip()
    if change == 'y':
        username = get_user(history)
    return username

def main_menu(history, username):
    cont = True
    while cont:
        print('-'*40)
        print("1. Calculator\n2. Show history\n3. Change user\n4. Quit")
        request = input('>>> ').strip()
        if request == "1":
            calc(history, username)
        elif request == '2':
            show_history(history, username)
        elif request == "3":
            username = change_user(history, username)
        elif request == "4":
            cont = False
        else:
            print("Incorrect request. Try again")

def main():
    history = CalcHistory()
    print("Hello, quest!")
    username = get_user(history)
    main_menu(history, username)

main()