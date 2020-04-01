from PIL import Image
from numpy import *
from scipy.ndimage import filters
from pylab import * 
im = array(Image.open('Desktop/Skin(3).jpg').convert('L'))
for i in range(1,8,2):
    im2 = filters.gaussian_filter(im,i)
    figure()
    gray()
    contour(im2, origin = 'image')
    axis('off')
    show()