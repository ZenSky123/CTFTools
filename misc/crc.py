import binascii
import codecs
import fire


def crack(crc, suffix, maxw=1024, maxh=1024):
    suffix = str(suffix)

    def tohex(i):
        return hex(i)[2:].rjust(8, '0')

    for w in range(maxw):
        for h in range(maxh):
            data = '49484452' + tohex(w) + tohex(h) + suffix
            data = codecs.decode(data, 'hex')
            crc32 = binascii.crc32(data) & 0xffffffff
            if crc32 == crc:
                print('w:{}   hex:{}'.format(w, tohex(w)))
                print('h:{}   hex:{}'.format(h, tohex(h)))
                return


if __name__ == '__main__':
    fire.Fire()
