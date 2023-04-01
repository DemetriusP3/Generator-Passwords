from random import choice
import string
import sys

def gen_password(spes_chars, len_passw):
    chars = '' if not bool(spes_chars) else '#$*-+=@?!&_'
    return ''.join(choice(string.ascii_letters + string.digits + chars) for _ in range(int(len_passw)))

def main(arg):
    len_passw, range_passw, spes_chars, saver, = arg[1:]
    if saver == 'print':
        for _ in range(int(range_passw)):
            print(gen_password(spes_chars, len_passw))
    elif saver == 'file':
        with open(f'{datetime.datetime.now()}.txt', 'a') as file:
            for _ in range(int(range_passw)):
                file.write(f'{gen_password(spes_chars, len_passw)}\n')


if __name__ == '__main__':
    main(sys.argv)
