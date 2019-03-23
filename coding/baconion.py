import fire


def peigen_encode(text):
    result = ''
    for i in text:
        result += '{0:05b}'.format(ord(i) - ord('a'))
    res = ''
    for i in result:
        if i == '0':
            res += 'A'
        else:
            res += 'B'
    return res


def peigen_decode(text):
    text = text.replace('A', '0').replace('B', '1')
    result = ''
    for i in range(0, len(text), 5):
        b = text[i: i + 5]
        result += chr(int(b, 2) + ord('a'))
    return result


if __name__ == '__main__':
    fire.Fire({
        'encode': peigen_encode,
        'decode': peigen_decode
    })
