import fire


def fence_decode(string):
    res = {}
    for n in range(2, len(string) - 1):
        ans = ''
        for i in range(n):
            for j in range(int(len(string) / n + 0.5)):
                try:
                    ans += string[j * n + i]
                except:
                    pass
        res[n] = ans
    return res


if __name__ == '__main__':
    fire.Fire({
        'decode': fence_decode,
        'encode': fence_decode
    })
