import pyAesCrypt
import json
import os


def get_tries():
    with open('data/tries.txt') as tries:
        return tries.read()


def subtract_tries():
    current_tries = int(get_tries())

    with open('data/tries.txt', 'w') as tries:
        tries.write(str(current_tries - 1))


def encrypt_file(key, remove=True):
    buffer_size = 64 * 1024

    pyAesCrypt.encryptFile("data/de_pws.json", "data/en_pws.json", key, buffer_size)

    if remove:
        os.remove("data/de_pws.json")


def decrypt_file(key):
    buffer_size = 64 * 1024

    pyAesCrypt.decryptFile("data/en_pws.json", "data/de_pws.json", key, buffer_size)


def save_to_decrypted(ids, custom_message=None):
    with open('data/de_pws.json', 'w') as f:
        json.dump(ids, f, indent=4)
    
    if custom_message:
        print(custom_message)
