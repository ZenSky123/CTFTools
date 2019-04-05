import fire


def chr_encode(*strings):
    string = ' '.join(map(str, strings))
    return ' '.join([str(ord(i)) for i in string])


def chr_decode(*nums):
    res = [chr(int(num)) for num in nums]
    return ''.join(res)


if __name__ == '__main__':
    fire.Fire({
        'encode': chr_encode,
        'decode': chr_decode
    })
