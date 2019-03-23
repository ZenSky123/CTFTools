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


def morse_encode(*strings):
    string = ' '.join(map(str, strings))
    x = string.split(' ')
    ccc = ''.join(x)
    return ' '.join(chars2morse(c) for c in ccc)


def morse_decode(*strings):
    strings = map(str, strings)
    return ''.join(morse2chars(c) for c in strings)


if __name__ == '__main__':
    fire.Fire({
        'encode': morse_encode,
        'decode': morse_decode
    })
