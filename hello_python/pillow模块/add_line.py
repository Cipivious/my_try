from PIL import Image, ImageDraw, ImageFilter

# 打开原始图像
img = Image.open("./cat.png")
w, h = img.size
draw = ImageDraw.Draw(img)
draw.line((0, 0) + img.size, width=2, fill="red")
draw.line((0, h, w, 0), width=2, fill="red")
img.show()
