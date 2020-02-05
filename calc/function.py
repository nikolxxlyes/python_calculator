import math

def add(a,b):
    return a + b

def dis(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

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

def get_user(history):
    username = ''
    while not username:
        print('-' * 40)
        print("If you have registered user, enter your 'username'. If want to be quest - press only enter.")
        request = input(">>> ").lower().strip()
        if request == '':
            username = 'quest'
        else:
            login = history.get_user(request)
            if login:
                print(f"Hello, {request}!")
                n = 3
                while n:
                    password = input('Enter your password>>> ').strip()
                    if history.check_password(password,login):
                        username = request
                        break
                    else:
                        print("Incorrect password")
                        n -= 1
                else:
                    print('Invalid login. Try again')
            else:
                print(f"User {request} is not found.")
                continue_reg = input('Do you want to register this username?(y/n) >>> ').strip()
                if continue_reg == 'y':
                    username = history.register(request)
    print(f'Welcome, {username}!')
    return username
