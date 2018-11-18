from PIL import Image, ImageDraw, ImageFont
import imageio
import random
import string

flag = "flag{th3y-t4k3_7he+J~tr4in}"

alpha = string.printable[:-6]
fnt = ImageFont.truetype('/usr/share/fonts/truetype/roboto-mono-elementary/RobotoMono-Regular.ttf', 24)

def make(size, text, name):
	img = Image.new('RGB', size, color=(255,255,255))
	d = ImageDraw.Draw(img)
	d.text((2,2), text, font=fnt, fill=(0,0,0))
	img.save(name)

n = 1
for i in range(0, len(flag), 7):
	make((105,30), flag[i:i+7], "{}a.png".format(n))
	n += 1


for i in range(4):
	for x in range(9):
		make((105,30), ''.join(random.sample(alpha,7)),"{}{}.png".format(i+1,alpha[x+11]))

for i in range(4):
	images = []
	for x in range(10):
		images.append(imageio.imread("{}{}.png".format(i+1, alpha[x+10])))
	imageio.mimsave('{}.gif'.format(i+1))
