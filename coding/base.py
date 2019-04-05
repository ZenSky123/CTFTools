import base64

import fire


def base_encode(*strings, encoding='utf-8'):
    string = ' '.join(map(str, strings))
    string = bytes(str(string), encoding)
    b16_res = base64.b16encode(string)
    b32_res = base64.b32encode(string)
    b64_res = base64.b64encode(string)
    b85_res = base64.b85encode(string)
    return {
        'b16': b16_res,
        'b32': b32_res,
        'b64': b64_res,
        'b85': b85_res
    }


def base_decode(*strings, encoding='utf-8'):
    def try_encode(encode_f):
        try:
            return encode_f(string)
        except:
            return None

    string = ' '.join(map(str, strings))

    string = bytes(str(string), encoding)
    b16_res = try_encode(base64.b16decode)
    b32_res = try_encode(base64.b32decode)
    b64_res = try_encode(base64.b64decode)
    b85_res = try_encode(base64.b85decode)
    return {
        'b16': b16_res,
        'b32': b32_res,
        'b64': b64_res,
        'b85': b85_res
    }


if __name__ == '__main__':
    fire.Fire({
        'encode': base_encode,
        'decode': base_decode
    })
