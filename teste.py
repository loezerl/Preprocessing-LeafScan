from skimage.color import rgb2gray
from skimage import data
from scipy import misc
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from skimage.filters import threshold_otsu

img = misc.imread("teste.jpg")

# img_gray = rgb2gray(img)

# plt.imshow(img_gray)
# plt.show()

def weightedAverage_pixel(pixel):
    return pixel[0]*0.299 + pixel[1]*0.587 + pixel[2]*0.114


grey = np.zeros((img.shape[0], img.shape[1])) # init 2D numpy array
# get row number
for rownum in range(len(img)):
   for colnum in range(len(img[rownum])):
      grey[rownum][colnum] = weightedAverage_pixel(img[rownum][colnum])


thresh = threshold_otsu(grey)
binary = grey > thresh

fig, axes = plt.subplots(ncols = 2)
ax = axes.ravel()

ax[0].imshow(img)
ax[0].set_title('Original')

ax[1].imshow(binary, cmap = plt.cm.gray)
ax[1].set_title('Binarizada')

#plt.imshow(grey, cmap= cm.Greys_r)

for a in ax:
    a.axis('off')

plt.show()