import pyqrcode
from pyqrcode import QRCode
import png

QRString = 'https://www.youtube.com/'

url = pyqrcode.create(QRString)

url.png(r'qr.png', scale=8)

