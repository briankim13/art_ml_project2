from PIL import Image
from os import listdir 
from resizeimage import resizeimage


imgs = [] 
files = listdir() 
for file in files:
	if file.endswith(".png"):
		imgs.append(file) 

idx = 0 
for im_name in imgs:
	im = Image.open(im_name)
	cover = resizeimage.resize_cover(im, [1024, 512])

	cover.save('changed/%s'%im_name, im.format) 
	print("saved as %s"%im_name)
	idx = idx + 1 



# with open('test-image.jpeg', 'r+b') as f:
#     with Image.open(f) as image:
#         cover = resizeimage.resize_cover(image, [200, 100])
#         cover.save('test-image-cover.jpeg', image.format)