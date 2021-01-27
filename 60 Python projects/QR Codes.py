import pyqrcode
from pyqrcode import QRCode

website="https://medium.com/coders-camp/60-python-projects-with-source-code-919cd8a6e512"

url=pyqrcode.create(website)

url.svg("60 Python Projects with Source code.svg", scale=9)
