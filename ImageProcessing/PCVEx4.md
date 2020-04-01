from PIL import Image
from numpy import *
from scipy.ndimage import filters
from pylab import * 
im = array(Image.open('Desktop/Buildings.png').convert('L'))

def outline(image):
    imx = zeros(im.shape)
    filters.sobel(im,1,imx)
    imy = zeros(im.shape)
    filters.sobel(im,0,imy)
    magnitude = 255 - sqrt(imx**2 + imy**2)

    figure()
    gray()
    imshow(magnitude)
    axis('off')
    show()

outline(im)

