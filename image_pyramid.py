import cv2
img = cv2.imread("./image/a.jpg")
low_res = cv2.pyrDown(img)
cv2.imshow("lowres", low_res)
cv2.waitKey()