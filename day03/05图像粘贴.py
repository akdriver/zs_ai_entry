from PIL import Image

dog = Image.open("dog.jpg")
cat = Image.open("cat.jpg")
dog.paste(cat,box=(100,100))
dog.show()


