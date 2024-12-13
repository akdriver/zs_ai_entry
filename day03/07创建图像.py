from array import array
from PIL import Image

import numpy as np

arr = np.zeros((600,400,3),dtype=np.uint8)
h,w,c = arr.shape
arr[:,:arr.shape[0]//2] = (255,0,0)
arr[:,arr.shape[1]//2:] = (255,255,0)
img = Image.fromarray(arr)
img.show()

