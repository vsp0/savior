# WARNING: This file will be removed after running.

import pyAesCrypt
import os

key = input('Come up with a safe and rememberable key: ')

while key == '':
    print('Something other than "".')

    key = input('Come up with a safe and rememberable key: ')


pyAesCrypt.encryptFile('data/de_pws.json', 'data/en_pws.json', key, 64 * 1024)


confirm = input("WARNING: This file will be removed. Continue? (y/n) ")

if confirm.strip().lower() == 'n':
    exit()


os.remove('data/de_pws.json')
os.remove('create_key.py')
