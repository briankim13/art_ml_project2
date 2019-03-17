# change buildings to sky
# change benz to road 
from PIL import Image
from os import listdir 
# from os.path import isfile, join 

# car: 26       1,0,140
# building: 11  70,70,70
# benz: 2       0,0,0
# road: 7       129,63,125
# sky: 23       68~70,130,179~180
# lawn: 22      150,250,152
# sidewalk: 8   244,35,232
# sidewalk?:6   81,0,81
# pole: 17      153,153,153 ~158
# other?: 4     0,0,0
# sign: 20      221,221,0
# tree: 21      105,142,36
# ppl:  25      221,22,65
# bicycle: 33   119,11,32  
# :        9    250,170,160
# guardrail:13  190,153,153  
#           5   111,74,0
#



imgs = [] 
files = listdir() 
for file in files:
	if file.endswith(".png"):
		imgs.append(file) 

idx = 0 
for im_name in imgs:
	im = Image.open(im_name)
	pix = im.load()

	for i in range(im.size[0]):
		for j in range(im.size[1]):
			# rgb = pix[i,j]
			# if 0 <= rgb[0] and rgb[0] <= 3:
			if pix[i,j] == 29 or pix[i,j] == 30 or pix[i,j] == 31:
				pix[i,j] = 21 
			elif pix[i,j] == 13 or pix[i,j] == 14:
				pix[i,j] = 7 
			elif pix[i,j] == 24 or pix[i,j] == 25 or pix[i,j] == 26:
				pix[i,j] = 17
			elif pix[i,j] == 27:
				pix[i,j] = 20 
			elif pix[i,j] == 18 or pix[i,j] == 19:
				pix[i,j] = 11
			elif pix[i,j] == 34 or pix[i,j] == 35 or pix[i,j] == 36:
				pix[i,j] = 26
			elif pix[i,j] == 32 or pix[i,j] == 33:
				pix[i,j] = 24 
			else:
				pix[i,j] = lastpix 

			lastpix = pix[i,j] 



	im.save('changed/%s'%im_name) 
	print("image saved to %s"%('changed/'+im_name)) 
	idx = idx + 1 

