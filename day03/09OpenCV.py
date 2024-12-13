import cv2


# 创建一个窗口
# cv2.namedWindow("sy",cv2.WINDOW_NORMAL)
# cv2.resizeWindow("sy",25,25)
# resized = cv2.resize(img,(25,25))
# cv2.imshow("sy",img)
# 等待一个Key 1000ms
# cv2.waitKey(2000)

img = cv2.imread("./dog.jpg")
cv2.imshow("ss",img)
cv2.waitKey()

# 通道分离# 通道分离
b,g,r = cv2.split(img)
cv2.imshow("b",b)
cv2.waitKey()

merged = cv2.merge((b,g,r))
cv2.imshow("ss4",merged)
cv2.waitKey()
cv2.destroyAllWindows()