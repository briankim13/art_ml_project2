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
	if file.endswith(".jpg"):
		imgs.append(file) 

idx = 0 
for im_name in imgs:
	im = Image.open(im_name).convert('L') 
	pix = im.load()

	for i in range(im.size[0]):
		for j in range(im.size[1]):
			# rgb = pix[i,j]
			# if 0 <= rgb[0] and rgb[0] <= 3:
				 
			if pix[i,j] == (1,0,140): # if its car
				pix[i,j] = 26

			elif pix[i,j] == (70,70,70): # if its building
				pix[i,j] = 11

			elif pix[i,j] == (0,0,0): # if it is benz 
				pix[i,j] = 2

			elif pix[i,j] == (129,63,125):  
				pix[i,j] = 7

			elif pix[i,j] == (70,130,180):  
				pix[i,j] = 23

			elif pix[i,j] == (150,250,152):  
				pix[i,j] = 22

			elif pix[i,j] == (244,35,232):  
				pix[i,j] = 8

			elif pix[i,j] == (81,0,81):  
				pix[i,j] = 6

			elif pix[i,j] == (153,153,153):  
				pix[i,j] = 17

			elif pix[i,j] == (221,221,0):  
				pix[i,j] = 20

			elif pix[i,j] == (105,142,36):  
				pix[i,j] = 21

			elif pix[i,j] == (221,22,64): 
				pix[i,j] = 25

			elif pix[i,j] == (119,11,32): 
				pix[i,j] = 33

			elif pix[i,j] == (250,170,160): 
				pix[i,j] = 9

			elif pix[i,j] == (190,153,153): 
				pix[i,j] = 13

			elif pix[i,j] == (111,74,0): 
				pix[i,j] = 5

			else:
				pix[i,j] = 4




	im.save('changed/%s'%im_name) 
	print("image saved to %s"%('changed/'+im_name)) 
	idx = idx + 1 

