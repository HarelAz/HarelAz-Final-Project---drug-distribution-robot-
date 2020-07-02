

def craetQR():
    qr = pyqrcode.create('Nikol')
    qr.png('Nikol.png',scale=10)


def decodeQR():
    d = decode(Image.open('Nikol.png'))
    print(d[0].data.decode('ascii'))


