import cv2
import numpy


def main():
    """
    Stream video from a phone camera over the network.
    Uses an IP webcam app on the phone (e.g., IP Webcam on Android).
    """
    # Fixed: 'l' -> '1' in the IP address
    url = "http://192.168.1.6:8888"

    # Open the video stream
    cap = cv2.VideoCapture(url)

    if not cap.isOpened():
        print(f"Error: Could not open video stream at {url}")
        print("Make sure your phone camera app is running and the IP is correct.")
        return

    print("Streaming phone camera. Press 'q' to quit.")

    while True:
        camera, frame = cap.read()
        if not camera or frame is None:
            print("Warning: Failed to read frame from stream.")
            break

        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1)
        if key == ord("q"):
            break

    # Clean up
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
