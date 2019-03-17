# import numpy as np
# import matplotlib.pyplot as plt
from os import listdir 
# from PIL import Image 
# from IPython.display import display

from matplotlib.pyplot import figure, imshow, axis
from matplotlib.image import imread

def showX(X, rows=1):
    assert X.shape[0]%rows == 0
    int_X = ( (X+1)/2*255).clip(0,255).astype('uint8')
    if channel_first:
        int_X = np.moveaxis(int_X.reshape(-1,3,imageSize,imageSize), 1, 3)
    else:
        int_X = int_X.reshape(-1,imageSize,imageSize, 3)
    int_X = int_X.reshape(rows, -1, imageSize, imageSize,3).swapaxes(1,2).reshape(rows*imageSize,-1, 3)
    display(Image.fromarray(int_X))

def showImages(list_of_files):
    fig = figure()
    number_of_files = len(list_of_files)
    for i in range(number_of_files):
        a=fig.add_subplot(1,number_of_files,i+1)
        image = imread(list_of_files[i])
        imshow(image,cmap='Greys_r')
        axis('off')
    print('image shown') 

# w=10
# h=10
# fig=plt.figure(figsize=(8, 8))
# columns = 4
# rows = 5
# for i in range(1, columns*rows +1):
#     img = np.random.randint(10, size=(h,w))
#     fig.add_subplot(rows, columns, i)
#     plt.imshow(img)
# plt.show()

# directory = 'image-data/hangul-images'
# files = listdir(directory) 
# w = 8 
# h = 4
# fig = plt.figure(figsize=(w,h))
# for i in range(32):
# 	im_name = directory + '/' + files[i]
# 	im = Image.open(im_name) 
# 	fig.add_subplot(h, w, i+1)
# 	plt.imshow(im) 

# plt.axis('off')
# # im.set_cmap('grey')
# plt.savefig("test.png", bbox_inches='tight')

# plt.show()

# directory = 'image-data/hangul-images'
# files = listdir(directory) 
# for i in range(10):
# 	files[i] = directory + '/' + files[i] 

# for file in files:
# 	file = directory + file 

directory = 'hangul'
files = listdir(directory) 
for i in range(len(files)):
	files[i] = directory + '/' + files[i] 
showImages(files)