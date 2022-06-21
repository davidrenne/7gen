from PIL import Image
name = 'hd-wallpaper-g32e2f6594_640'
img = Image.open("images/" + name + ".jpeg")
img = img.resize((544, 306), Image.ANTIALIAS)
img.save("images/" + name + ".bmp")

img = img.resize((128, 72), Image.ANTIALIAS)
img.save("images/" + name + "-preview.bmp")
