def calculator(number, oper, number2=None, more_option=False):
    import math
    if number2 is not None:
        str_oper = f"{str(number)}{oper}{str(number2)}"
    else:
        str_oper = f"{oper}({str(number)})"
    if oper == '+':
        res = number + number2
    elif oper == '-':
        res = number - number2
    elif oper == '/' or oper == ':':
        try:
            res = number / number2
        except ZeroDivisionError :
            return "Division by zero isn't possible"
    elif oper == '*' or oper == 'x':
        res = number * number2
    elif oper == 'sin':
        if more_option:
            res = math.sin(number)
        else:
            return f"Operation '{oper}' for only register user"
    elif oper == 'cos':
        if more_option:
            res =  math.cos(number)
        else:
            return f"Operation '{oper}' for only register user"
    elif oper == 'tan':
        if more_option:
            res =  math.tan(number)
        else:
            return f"Operation '{oper}' for only register user"
    elif oper == 'ctan':
        if more_option:
            res =  1 / math.tan(number)
        else:
            return f"Operation '{oper}' for only register user"
    else:
        return f"{oper} is not supported in this calculator"

    return [f"{str_oper}={round(res,2)}"]

def get_data_oper(more_option):
    if more_option:
        operations = '+,-,*,/ and sin,cos,tan,ctan'
    else:
        operations = '+,-,*,/'
    try:
        number = float(input("Enter first number >>> ").strip())
        oper = input(f"Enter operation ({operations})>>> ").strip()
        if oper != 'sin' and oper != 'cos' and oper != 'tan' and oper != 'ctan':
            number2 = float(input("Enter second number >>> ").strip())
            return number, oper, number2
        return number, oper
    except ValueError:
        pass
    except Exception as error:
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
            user = history.is_user(request)
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
                    print('Try again')
            else:
                print(f"User {request} is not found.")
                register = input('Do you want register this username?(y/n) >>> ')
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
                        print('Try again')
    print(f'Welcome, {username}!')
    return username
