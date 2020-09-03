from lib.files import get_tries, subtract_tries
from lib.files import encrypt_file, decrypt_file
from lib import commands


access_granted = False

while not access_granted and int(get_tries()) != 0:
    passwd = input('Key: ')

    try:
        decrypt_file(passwd)

        access_granted = True

    except:
        # Wrong key: -1 tries
        subtract_tries()

        print('Incorrect key... tries left: ' + get_tries())

 
if not access_granted:
    print('No more tries left.')

    exit()


while True:
    valid_commands = {
        'exit': commands._exit,
        'new_id': commands.new_id,
        'edit': commands.edit_id,
        'help': commands._help,
    }

    cmd = input('>>> ')

    if cmd == '':
        pass
    
    elif cmd in valid_commands.keys():
        valid_commands[cmd]()

    else:
        print('Command not found.')

    encrypt_file(passwd, remove=False)
