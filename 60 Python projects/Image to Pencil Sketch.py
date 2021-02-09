import cv2
im = cv2.imread("abdo.jpg")

image = cv2.resize(im, (960, 740))
cv2.waitKey(0)

gray_image=cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
#cv2.imshow("gray", gray_image)
#cv2.waitKey(0)

inverted_image= 255 - gray_image
#cv2.imshow("Inverted", inverted_image)
#cv2.waitKey(0)

blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
#cv2.imshow("Sketch", pencil_sketch)
#cv2.waitKey(0)

outpath = "Pencil Sketch.jpg"
cv2.imwrite(outpath, pencil_sketch)

cv2.imshow("Original image", image)
cv2.imshow("Pencil Sketch", pencil_sketch)
cv2.waitKey(0)
