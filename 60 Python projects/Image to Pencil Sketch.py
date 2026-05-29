"""Convert a color image into a pencil sketch effect using OpenCV."""

import os
import cv2


def convert_to_pencil_sketch(
    input_image: str,
    output_image: str = "Pencil Sketch.jpg",
    display: bool = True,
) -> None:
    """Convert an image to a pencil sketch and save/display the result."""
    if not os.path.exists(input_image):
        print(f"Error: input image '{input_image}' not found.")
        return

    img = cv2.imread(input_image)
    if img is None:
        print(f"Error: could not read image '{input_image}'.")
        return

    # Resize the image for consistent output
    image = cv2.resize(img, (960, 740))

    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    # Invert the grayscale image
    inverted_image = 255 - gray_image

    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

    # Invert the blurred image
    inverted_blurred = 255 - blurred

    # Create the pencil sketch using the dodge blend mode
    pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

    # Save the result
    cv2.imwrite(output_image, pencil_sketch)
    print(f"Pencil sketch saved to '{output_image}'.")

    if display:
        cv2.imshow("Original image", image)
        cv2.imshow("Pencil Sketch", pencil_sketch)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    convert_to_pencil_sketch("abdo.jpg")
