"""Apply Instagram-style filters to images using the instafilter library."""

import cv2

# Try to import the instafilter library; it may not be installed
try:
    from instafilter import Instafilter
except ImportError:
    print("Error: 'instafilter' library is not installed.")
    print("Install it with: pip install instafilter")
    exit(1)


def apply_filter(input_image: str, filter_name: str = "Lo-fi", output_image: str = "Filtered_image.jpg") -> None:
    """Apply an Instagram-style filter to an image and save the result."""
    model = Instafilter(filter_name)
    new_image = model(input_image)
    cv2.imwrite(output_image, new_image)
    print(f"Filtered image saved as '{output_image}'")


if __name__ == '__main__':
    apply_filter("abdo 1.jpg")
