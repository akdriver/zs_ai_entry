from PIL import Image,ImageFont,ImageDraw

img = Image.open("cat.jpg")
drawer = ImageDraw.Draw(img)

font = ImageFont.truetype("./NewYork.ttf",size=40)
text_to_write = "Hello World!"
position = (0,0)
color = (255,0,0)

drawer.text(position,text_to_write,fill=color,font=font)
img.show()