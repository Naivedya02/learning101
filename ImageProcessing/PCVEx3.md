from PIL import Image
from numpy import *
from scipy.ndimage import filters
from pylab import * 
sigma = 110
im = array(Image.open('Desktop/Hands and Skins/Skin(4).jpg').convert('L'))
im2 = filters.gaussian_filter(im,sigma)
im3 = ndarray((len(im), len(im[0])))
for i in range(0,len(im)):
    for j in range(0, len(im[0])):    
        if im2[i][j]!=0:
            im3[i][j] = im[i][j]/im2[i][j]
        else:
            im3[i][j] = im[i][j]
figure()
gray()
imshow(im)
axis('off')
show()

figure()
gray()
imshow(im2)
axis('off')
show()

figure()
gray()
imshow(im3)
axis('off')
show()
