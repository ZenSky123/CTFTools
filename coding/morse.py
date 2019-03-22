import re
import fire

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
codes = """.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-..
-- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..
.---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----"""

dd = dict(zip(chars.lower(), codes.split()))
DD = dict(zip(codes.split(), chars.lower()))


def chars2morse(char):
    return dd.get(char.lower(), ' ')


def morse2chars(morse):
    return DD.get(morse, ' ')


def morse(string):
    string = str(string)
    x = string.split(' ')
    ccc = ''.join(x)
    if re.match('^[0-9a-zA-Z]+$', ccc):
        return ' '.join(chars2morse(c) for c in ccc)
    else:
        cc = string.split()
        return ' '.join(morse2chars(c) for c in cc)


if __name__ == '__main__':
    fire.Fire(morse)
