import cv2

camera = cv2.VideoCapture(1)
# camera = cv2.VideoCapture("path to video")

while True:
    # 如果没有结束，retval == True 如果读取完成，retVal == False
    retval,image  =  camera.read()
    if not retval:
        break
    cv2.imshow("ss",image)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cv2.destroyAllWindows()