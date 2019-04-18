from PIL import Image


def generate(string, reverse=False):
    length = None
    for i in range(10000):
        if i * i == len(string):
            length = i
            break

    if length is None:
        return "Length Error!"

    pixel_list = [(0, 0, 0), (255, 255, 255)]
    if reverse:
        pixel_list = pixel_list[::-1]

    res = Image.new('RGB', (length, length))
    for i in range(length):
        for j in range(length):
            cur = string[i * length + j]
            res.putpixel((j, i), pixel_list[int(cur)])
    res.save('res.png')
