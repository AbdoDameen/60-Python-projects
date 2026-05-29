import pyqrcode
from pyqrcode import QRCode


def main():
    """Generate a QR code SVG for a given URL."""
    website = "https://medium.com/coders-camp/60-python-projects-with-source-code-919cd8a6e512"

    # Create the QR code from the website URL
    url = pyqrcode.create(website)

    # Save as an SVG file with a scale of 9
    url.svg("60 Python Projects with Source code.svg", scale=9)


if __name__ == '__main__':
    main()
