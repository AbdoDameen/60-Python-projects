import cv2
from instafilter import Instafilter

model=Instafilter("Lo-fi")
new_image = model("abdo 1.jpg")

cv.imwrite("Filtered_image.jpg", new_image)
