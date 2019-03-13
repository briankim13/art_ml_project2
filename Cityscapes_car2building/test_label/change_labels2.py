# change buildings to sky
# change benz to road 
from PIL import Image
from os import listdir 
# from os.path import isfile, join 

# car: 26
# building: 11
# benz: 2
# road: 7
# sky: 23
# tree: 21

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
			if pix[i,j] == 26: # if its car
				pix[i,j] = 11 # make it to building
			elif pix[i,j] == 11: # if its building
				pix[i,j] = 21 # make it to tree
			elif pix[i,j] == 2: # if it is benz 
				pix[i,j] = 7 # make it into road

	im.save('changed/%s'%im_name) 
	print("saved as %s"%im_name)
	idx = idx + 1 

