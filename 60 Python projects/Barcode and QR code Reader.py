"""
Barcode and QR code Reader.
Uses OpenCV and pyzbar to decode barcodes and QR codes from a webcam feed.
"""

import cv2
from pyzbar import pyzbar


def read_barcodes(frame):
    """
    Detect and decode barcodes/QR codes in a video frame.
    Draws bounding boxes and labels. Returns the annotated frame.
    """
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        barcode_info = barcode.data.decode("utf-8")
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
        with open("barcode_result.txt", mode='w') as file:
            file.write("Recognized barcode: " + barcode_info)

    return frame


def main():
    """Open camera, read frames, detect barcodes, display until ESC is pressed."""
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()

    while ret:
        ret, frame = camera.read()
        frame = read_barcodes(frame)
        cv2.imshow("Barcode/QR code reader", frame)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC key
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
