from PIL import Image
import zbarlight
import fire


def scan_QRcode(file_path):
    with open(file_path, 'rb') as image_file:
        image = Image.open(image_file)
        image.load()

    codes = zbarlight.scan_codes('qrcode', image)
    return codes


if __name__ == '__main__':
    fire.Fire(scan_QRcode)
