import codecs
import fire


def rot_decode(string):
    string = str(string)
    return codecs.encode(string, 'rot-13')


if __name__ == '__main__':
    fire.Fire({
        'encode': rot_decode,
        'decode': rot_decode
    })
