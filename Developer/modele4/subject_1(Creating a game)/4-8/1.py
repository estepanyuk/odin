from PIL import Image, ImageDraw

img = Image.new('RGB',(90, 90), 'white')
draw = ImageDraw.Draw(img)

draw.ellipse((0, 0, 90, 90), 'yellow', 'blue')
draw.ellipse((25, 20, 35, 30), 'yellow', 'blue')
draw.ellipse((50, 20, 60, 30), 'yellow', 'blue')
draw.arc((20, 40, 70, 70), 0, 180, 0)

img.save('img7.jpg')

