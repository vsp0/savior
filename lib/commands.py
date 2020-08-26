from . import files
from . import ids

import random
import json
import os


def edit_id():
    print('Options: first_name, last_name, email or password')

    edit = input('Edit: ')
    
    editable = ['first_name', 'last_name', 'email', 'password']

    while edit not in editable:
        print('Please, choose one of the following: first_name, last_name, email or password')
        
        edit = input('Edit: ')

    if edit in editable:
        id_name = input('ID name: ')
        
        de = json.load(open('data/de_pws.json'))

        while id_name not in de.keys():
            print('ID name doesen\'t exist.')

            id_name = input('ID name: ')

        if id_name in de.keys():
            if edit == 'password':
                new_password = input('New password: ')
                confirm_password = input('Confirm: ')

                while new_password != confirm_password:
                    print('Passwords didn\'t match.')

                    new_password = input('New password: ')
                    confirm_password = input('Confirm: ')

                if new_password == confirm_password:
                    de[id_name]['password'] = new_password

                    files.save_to_decrypted(de, 'Password has been changed.')
            
            else:
                new_value = input(f'Enter new {edit}: ')
                
                de[id_name][edit] = new_value

                files.save_to_decrypted(de, f'{edit} has been changed.')


def new_id():
    print('The \'/\' in the start means that it\'ll be random it it\'s not specified.\n')

    de_pws = json.load(open('data/de_pws.json'))

    name = input('/ Call the new ID for something: ')

    if name == '':
        name = str(random.randint(1000000000, 9999999999))

    while name in de_pws.keys():
        print('ID already exists.')

        name = input('/ Call the new ID for something: ')


    first_name = ids.get_first_name()
    last_name = ids.get_last_name()

    email = input('Email: ')
    password = ids.get_password()
    
    id_ = {
        'id_name': name,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': password,
    }
    
    de_pws[name] = id_

    files.save_to_decrypted(de_pws, 'Created new ID.')


def _exit():
    os.remove('data/de_pws.json')

    exit()
