from PIL import Image, ImageDraw
from PIL import ImageColor
import random

# 获取所有支持的颜色名称
color_list = list(ImageColor.colormap.keys())
print(color_list)

img = Image.new(mode="RGB", size=(300, 300), color="white")
draw = ImageDraw.Draw(img)


# def get_color(point):
#     point_x = point[0]
#     point_y = point[1]
#     if point_x < 100 and point_y < 100:
#         return (255, 0, 0)
#     if point_x < 200 and point_y < 100:
#         return (0, 255, 0)
#     if point_x <= 300 and point_y < 100:
#         return (0, 0, 255)
#     if point_x < 100 and point_y < 200:
#         return (0, 255, 0)
#     if point_x < 200 and point_y < 200:
#         return (255, 255, 0)
#     if point_x <= 300 and point_y < 200:
#         return (0, 255, 255)
#     if point_x < 100 and point_y <= 300:
#         return (0, 0, 255)
#     if point_x < 200 and point_y <= 300:
#         return (0, 255, 255)
#     if point_x <= 300 and point_y <= 300:
#         return (255, 0, 255)

color = random.choices(color_list, k=5)


def get_color(point):
    point_x = int(point[0] / 100)
    point_y = int(point[1] / 100)
    return color[point_x + point_y]


for i in range(300):
    for j in range(300):
        draw.point((i, j), fill=get_color((i, j)))

img.show()
