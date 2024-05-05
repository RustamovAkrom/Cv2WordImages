import cv2

img = cv2.imread("images/img2.png")

img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

img = cv2.cvtColor(img, cv2.COLOR_LAB2BGR)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

r, g, b = cv2.split(img)

cv2.imshow("Result", b)
cv2.waitKey(0)