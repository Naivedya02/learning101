from PIL import Image
from numpy import *
from scipy.ndimage import filters
from pylab import * 
sigma = 5
im = array(Image.open('Desktop/Hands and Skins/Skin(1).jpg').convert('L'))
im2 = filters.gaussian_filter(im,sigma)
im3 = im - im2

figure()
gray()
imshow(im3)
axis('off')
show()

imc = array(Image.open('Desktop/Hands and Skins/Skin(1).jpg'))
im2c = zeros(imc.shape)
for i in range(3):
    im2c[:,:,i] = filters.gaussian_filter(imc[:,:,i],sigma)
    im2c = uint8(im2c)
im3c = imc - im2c

figure()
gray()
imshow(im3c)
axis('off')
show()