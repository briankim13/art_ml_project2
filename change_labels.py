from PIL import Image
from os import listdir 
# from os.path import isfile, join 

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
				pix[i,j] = 21 # make it to trees

	im.save('changed/%s'%im_name) 
	idx = idx + 1 

# im = Image.open('frankfurt_000000_000576_gtFine_labelIds.png') # Can be many different formats.
# pix = im.load()

# for i in range(im.size[0]):
# 	for j in range(im.size[1]):
# 		if pix[i,j] == 26: # if its car
# 			pix[i,j] = 11 # make it to building
# 		elif pix[i,j] == 11: # if its building
# 			pix[i,j] = 21 # make it to sky

# im.save('frankfurt_change_1_labelIds.png')  # Save the modified pixels as .png