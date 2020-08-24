import random
import string
import names

symbols = string.ascii_letters + string.digits + string.punctuation


def get_first_name():
    return names.get_first_name()


def get_last_name():
    return names.get_last_name()


def get_password(length):
    return ''.join(random.choices(symbols, k=int(length)))

