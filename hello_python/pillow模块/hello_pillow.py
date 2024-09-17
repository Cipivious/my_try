from PIL import Image

img1 = Image.open("./image.png").convert(mode="RGB")
# img1.show()
img2 = Image.new("RGB", img1.size, "red")
print(img1.size)
Image.blend(img1, img2, alpha=0.5).show()
