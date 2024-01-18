from PIL import Image, ImageDraw

# 1 вариант
pil = Image.new("RGB", (90, 90), color=("#FFFFFF"))
draw = ImageDraw.Draw(pil)

draw.ellipse((0, 0, 90, 90), 'yellow', 'blue')
draw.ellipse((25, 20, 35, 30), 'yellow','blue')
draw.ellipse((50, 20, 60, 30), 'yellow', 'blue')
draw.arc((20, 40, 80, 50), 0, 180, 0)
pil.save('smile3.jpg')

# 2 вариант
pil = Image.new("RGB", (200, 200), color="white")
draw = ImageDraw.Draw(pil)
draw.ellipse((50, 50, 200, 200), fill='yellow', outline=(0, 0, 0))
draw.ellipse((100, 100, 110, 110), fill='white', outline=(0, 0, 0))
draw.ellipse((150, 100, 160, 110), fill='white', outline=(0, 0, 0))
draw.arc(xy=(100, 150, 160, 150), start = 30, end = 270, fill="red")
pil.show()