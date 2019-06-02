from PIL import Image, ImageEnhance
import colorsys
import sys

H = (0, 0, 0)
S = (0, 0, 0)
V = (0, 0, 0)

def emotion(num):
	global H, S, V
	if num == '1': #Happiness
		H = (107, 57, 5)
		S = (39, 100, 65)
		V = (82, 100, 98)
	elif num == '3': #Anger
		H = (0, 25, 357)
		S = (0, 100, 100)
		V = (0, 95, 90)
	elif num == '4': #Disgust
		H = (262, 286, 183)
		S = (86, 43, 96)
		V = (27, 43, 9)
	elif num == '5': #Fear
		H = (0, 209, 274)
		S = (0, 94, 75)
		V = (0, 25, 55)
	elif num == '6': #Sadness
		H = (0, 0, 0)
		S = (0, 0, 0)
		V = (32, 95, 73)
	print (H, S, V)

def retouch(img, num):
	i = 1
	j = 1
	width = img.size[0]
	height = img.size[1]
	for i in range(0, width):
		for j in range(0, height):
			(r, g, b) = img.getpixel((i, j))
			(h, s, v) = colorsys.rgb_to_hsv(r/255, g/255, b/255)
			minDis = 180
			for m in range(0, 3):
				hueDis = min(abs(h * 360 - H[m]), 360 - abs(h * 360 - H[m]))
				if hueDis < minDis:
					minDis = hueDis
					hueNum = m
			h = H[hueNum] / 360
			# s = S[hueNum] / 100
			# v = V[hueNum] / 100
			if h == 0:
				s = 0
			(rr, gg, bb) = colorsys.hsv_to_rgb(h, s, v)
			img.putpixel((i, j), (int(rr * 255), int(gg * 255), int(bb * 255)))


def main(argv):
	path = argv[1]
	emotion(argv[2])
	img = Image.open(path + '/base.jpg')
	print (img.size)
	retouch(img, argv[2])

	img = img.convert('RGB')
	path_save = path + '/H_0' + str(argv[2])
	img.save(path_save + '.jpg')

	# img_12 = ImageEnhance.Color(img).enhance(1.2)
	# img_12.save(path_save + '_s1.2' + '.jpg')
	# img_15 = ImageEnhance.Color(img).enhance(1.5)
	# img_15.save(path_save + '_s1.5' + '.jpg')
	# img_18 = ImageEnhance.Color(img).enhance(1.8)
	# img_18.save(path_save + '_s1.8' + '.jpg')
	# img_20 = ImageEnhance.Color(img).enhance(2.0)
	# img_20.save(path_save + '_s2.0' + '.jpg')

	# img_12 = ImageEnhance.Brightness(img).enhance(1.2)
	# img_12.save(path_save + '_v1.2' + '.jpg')
	# img_15 = ImageEnhance.Brightness(img).enhance(1.5)
	# img_15.save(path_save + '_v1.5' + '.jpg')
	# img_18 = ImageEnhance.Brightness(img).enhance(1.8)
	# img_18.save(path_save + '_v1.8' + '.jpg')
	# img_20 = ImageEnhance.Brightness(img).enhance(2.0)
	# img_20.save(path_save + '_v2.0' + '.jpg')

if __name__=="__main__":
	main(sys.argv)




