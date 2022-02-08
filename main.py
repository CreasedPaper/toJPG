from PIL import Image
import os

filename = input("name of image you want to convert(make sure to include the current file extension ex: .png)")
image = Image.open(filename)
imagesize = os.path.getsize(filename)
rgb = image.convert("RGB")
rgb.save(filename + ".jpg")

