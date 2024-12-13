from PIL import Image

png= Image.open("IMG_0121.PNG")
r,g,b = png.split()
r.show()
g.show()
b.show()

merged_image = Image.merge("RGB",(r,g,b))
merged_image.show()

