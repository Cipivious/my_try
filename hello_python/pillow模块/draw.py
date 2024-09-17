from PIL import Image, ImageDraw, ImageFilter

# 打开原始图像
img = Image.open("./cat.png").convert("RGBA")

# 创建一个白色背景的图像，与原图大小相同
white_background = Image.new("RGBA", img.size, "white")

# 创建一个遮罩图像，与原图大小相同
mask = Image.new("L", img.size, 0)

# 创建绘图对象
draw = ImageDraw.Draw(mask)
w, h = img.size
# 设置圆角的半径
corner_radius = 50

# # 绘制圆角矩形的遮罩
# draw.rounded_rectangle([(0, 0), img.size], radius=corner_radius, fill=255)
draw.pieslice((0, 0, corner_radius, corner_radius), start=180, end=270, fill=255)
draw.pieslice((0, h - corner_radius, corner_radius, h), start=90, end=180, fill=255)
draw.pieslice((w - corner_radius, h - corner_radius, w, h), start=0, end=90, fill=255)
draw.pieslice((w - corner_radius, 0, w, corner_radius), start=270, end=360, fill=255)
draw.rectangle((0, corner_radius / 2, w, h - corner_radius / 2), fill=255)
draw.rectangle((corner_radius / 2, 0, w - corner_radius / 2, h), fill=255)

# 对遮罩进行模糊处理，使边缘更加平滑
mask = mask.filter(ImageFilter.DETAIL)

# 将原图粘贴到白色背景上，并使用遮罩
white_background.paste(img, (0, 0), mask=mask)

# 转换为RGB模式去掉透明度
final_img = white_background.convert("RGB")

# 显示最终的圆角图像
final_img.show()
