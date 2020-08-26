import random
import string
import names

symbols = string.ascii_letters + string.digits + string.punctuation


def get_first_name():
    first_name = input('/ First name: ')

    if first_name == '':
        first_name = names.get_first_name()
    
    return first_name


def get_last_name():
    last_name = input('/ Last name: ')

    if last_name == '':
        last_name = names.get_last_name()

    return last_name

def get_password():
    password = input('/ Password: ')

    if password == '':
        while True:
            try:
                length = int(input('Length of password: '))

            except ValueError:
                print('Please, enter a number.')

                continue

            else:
                password = ''.join(random.choices(symbols, k=int(length)))

                break

    return password

print(get_password())
