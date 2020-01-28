import math

def add(a,b):
    return a + b

def dis(a,b):
    return a - b

def mul(a,b):
    return a - b

def div(a,b):
    return a - b

def sin(a):
    return math.sin(a)

def cos(a):
    return math.cos(a)

def tan(a):
    return math.tan(a)

def ctan(a):
    return 1 / math.tan(a)

def calculator(more_option):
    operations = {
        '+': add,
        '-': dis,
        '*': mul,
        '/': div,
    }
    reg_oper = {
        'sin': sin,
        'cos': cos,
        'tan': tan,
        'ctan': ctan
    }
    if more_option:
        operations.update(reg_oper)
    num1,oper,*num2 = get_data_oper(operations,reg_oper)
    if num2:
        str_oper = f"{str(num1)}{oper}{str(*num2)}"
    else:
        str_oper = f"{oper}({str(num1)})"
    try:
        res = operations[oper](num1,*num2)
        return f"{str_oper}={round(res, 2)}"
    except KeyError:
        raise KeyError(oper)
    # except Exception as error:
    #     print("calc")
    #     print(type(error), error)

def get_data_oper(operations,reg_oper):
    oper_list = operations.keys()
    try:
        num1 = float(input("Enter first number >>> ").strip())
        oper = input(f"Enter operation ({' '.join(oper_list)})>>> ").strip()
        if oper not in reg_oper:
            num2 = float(input("Enter second number >>> ").strip())
            return num1, oper, num2
        return num1, oper
    except ValueError:
        pass
    # except Exception as error:
    #     print(1)
    #     print(type(error), error)

def get_user(history):
    username = ''
    while not username:
        print('-' * 40)
        print("If you have registered user, enter your 'username'. If want to be quest - press only enter.")
        request = input(">>> ").lower().strip()
        if request == '':
            username = 'quest'
        else:
            user = history.get_user(request)
            if user:
                print(f"Hello, {request}!")
                n = 3
                while n:
                    password = input('Enter your password>>> ')
                    if history.check_password(password,user):
                        username = request
                        break
                    else:
                        print("Incorrect password")
                        n -= 1
                else:
                    print('Invalid login. Try again')
            else:
                print(f"User {request} is not found.")
                register = input('Do you want to register this username?(y/n) >>> ')
                if register == 'y':
                    point = 3
                    while point:
                        pass1 = input('Create password (8+ symbol)>>> ')
                        pass2 = input('Repeat password >>> ')
                        if pass1 != pass2:
                            print('pass1 != pass2')
                            point -= 1
                        elif len(pass1) < 8:
                            print('len(pass1) < 8')
                            point -= 1
                        else:
                            username = request
                            history.reg_user(username, pass1)
                            print(f"Congratulation, you're registered now as {username}.")
                            break
                    else:
                        print('Invalid registration. Try again')
    print(f'Welcome, {username}!')
    return username
