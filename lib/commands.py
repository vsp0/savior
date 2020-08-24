from .files import encrypt_file
import random
import json
import os


def _exit():
    os.remove('data/de_pws.json')

    exit()


def new_id():
    print('The \'/\' in the start means that it\'ll be random it it\'s not specified.\n')

    de_pws = json.load(open('data/de_pws.json'))

    name = input('/ Call the new id for something: ')

    if name == '':
        name = str(random.randint(1000000000, 9999999999))

    while name in de_pws.keys():
        print('ID already exists.')

        name = input('/ Call the new id for something: ')


    first_name = input('/ First name: ')
    last_name = input('/ Last name: ')

    email = input('Email: ')
    password = input('/ Password: ')
    
    id_ = {
        'id_name': name,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': password,
    }
    
    de_pws[name] = id_

    with open('data/de_pws.json', 'w') as de:
        json.dump(de_pws, de, indent=4)
