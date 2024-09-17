from PIL import Image

img1 = Image.open("./cat.png")
img2 = Image.open("./image.png")
img2 = img2.resize(img1.size)
r, g, b = img2.split()

img = Image.composite(img2, img1, b).resize((img1.size[0] * 5, img1.size[1] * 5))
img.save("./result.png")
