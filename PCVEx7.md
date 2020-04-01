from PIL import Image
from numpy import *
from scipy.ndimage import *
from pylab import *

im = array(Image.open('Desktop/Buildings.png').convert('L'))
im_open = (morphology.binary_opening(255 - im, ones((5,2)),iterations=3))
labels_open, nbr_objects_open = measurements.label(im_open)

arr = measurements.center_of_mass(im_open, labels_open, range(1,nbr_objects_open))

figure()
gray()
imshow(im)
axis('off')
for i in range(0,len(arr)):
    plot(arr[i][1],arr[i][0], 'go')
title('Center of Mass of Objects')
show()