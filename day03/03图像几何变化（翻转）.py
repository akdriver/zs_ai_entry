import PIL.Image
from PIL import Image

img = Image.open("./IMG_0121.PNG")

rimg = img.transpose(PIL.Image.Transpose.ROTATE_90)
# 旋转角度0，图片向左 和向下平移100个单位. 平移的部分填充一个颜色
rimg = img.rotate(0,translate=(100,100),fillcolor="#DC143C")

rimg.show()

