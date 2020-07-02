from PIL import Image
from pyzbar.pyzbar import decode

d=decode(Image.open('Nikol.png'))
print(d[0].data.decode('ascii'))


