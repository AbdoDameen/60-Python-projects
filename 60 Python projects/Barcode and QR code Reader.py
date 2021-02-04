import cv2
from pyzbar import pyzbar

def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        barcode_info = barecode.data.decode("utf_8")
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)

        font=cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x+6, y-6), font, 2.0, (255, 255, 255), 1)
        with open("barcode_result.txt", mode='w') as file:
            file.write("Recognized barcode: "+ barcode_info)

def main():
    camera=cv2.VideoCapture(0)
    ret, frame = camera.read()
    while ret:
        ret, frame = camera.read()
        frame = read_barcodes(frame)
        cv2.imshow("Barcode/QR code reader", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    camera.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()
