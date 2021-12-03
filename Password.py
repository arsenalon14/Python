### Make function that import lenght for password and website that use this password.

def password():
    import random
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = lower.upper()
    number = '0123456789'
    symbol = '@#$%^&*{}[]'
### combine all character togdther
    all_cha = lower + upper + number + symbol
### user input lenght of character 
    length = int(input('Input length of password: '))
    name1 = str(input('Web site to use this password is: '))
    password = ''.join(random.sample(all_cha, length))

    return print(f'Password for {name1} is {password}')
 

print('Program to make your password')
password()
