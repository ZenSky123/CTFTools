import fire


def caesar_decode(string):
    string = string.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    res = {}
    for offset in range(26):
        alpha_table = {alphabet[i]: alphabet[(i + offset) % 26] for i in range(26)}
        newstring = ''.join(alpha_table[i] if i in alpha_table else i for i in string)
        res[offset] = newstring
    return res


if __name__ == '__main__':
    fire.Fire({
        'encode': caesar_decode,
        'decode': caesar_decode
    })
