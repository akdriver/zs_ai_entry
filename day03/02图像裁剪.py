from PIL import Image

image  = Image.open("IMG_0121.PNG")
w,h = image.size

box = (0,0,w//2,h)
crop_image = image.crop(box=box)
crop_image.show()

box2 = (w//2,0,w,h)
crop_image2 = image.crop(box2)
crop_image2.show()
