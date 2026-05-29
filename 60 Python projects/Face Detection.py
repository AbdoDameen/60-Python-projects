"""Detect faces in an image using OpenCV Haar cascades."""

import os
import cv2


def detect_faces(
    input_image: str,
    cascade_path: str = "haarcascade_frontalface_default.xml",
    output_image: str = "face_detected.png",
) -> None:
    """Detect faces in an image, draw rectangles around them, and save the result."""
    # Check that the cascade XML file exists
    if not os.path.exists(cascade_path):
        print(f"Error: Haar cascade file '{cascade_path}' not found.")
        print("Download it from: https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml")
        return

    # Check that the input image exists
    if not os.path.exists(input_image):
        print(f"Error: input image '{input_image}' not found.")
        return

    face_cascade = cv2.CascadeClassifier(cascade_path)
    img = cv2.imread(input_image)

    if img is None:
        print(f"Error: could not read image '{input_image}'.")
        return

    # Detect faces
    faces = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=4)

    if len(faces) == 0:
        print("No faces detected.")
    else:
        print(f"Detected {len(faces)} face(s).")

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Save and display the result
    cv2.imwrite(output_image, img)
    print(f"Result saved to '{output_image}'.")

    cv2.imshow("Face Detection", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    detect_faces("abdo 1.jpg")
