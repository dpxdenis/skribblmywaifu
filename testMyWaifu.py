from PIL import Image

img = Image.open('waifu.jpg')
grrr = img.convert('L')
bw = grrr.point(lambda x: 0 if x<170 else 255, '1')
finish = bw.resize((300,300),Image.ANTIALIAS)
finish.show()