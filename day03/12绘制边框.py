
import cv2


cat = cv2.imread("cat.jpg")
cat[:,:24,:] = (255,0,0)
cat[:,-24:,:] = (120,0,0)

cat[:24,24:-24,:] = (234,23,90)
cat[-24:,24:-24,:] = (35,120,90)
#
cv2.imshow("cat",cat)
cv2.waitKey()
cv2.destroyAllWindows()
# a = [1,2,3,4]
#
# print(a[:-2])