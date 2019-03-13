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
				pix[i,j] = 26 # make it to car
			elif pix[i,j] == 2: # if it is benz 
				pix[i,j] = 7 # make it into road

	im.save('changed/%s'%im_name) 
	idx = idx + 1 

