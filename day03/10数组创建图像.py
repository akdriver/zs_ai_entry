import cv2
import numpy as np

img = np.full(shape = (500,500,3),fill_value=100,dtype=np.uint8)
cv2.imshow("Ss",img)
cv2.waitKey()
cv2.destroyAllWindows()