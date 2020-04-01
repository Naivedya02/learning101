from PIL import Image
from numpy import *
from scipy.ndimage import filters, measurements, morphology
from pylab import *

im = array(Image.open('Desktop/Binary.png').convert('L'))
im = uint8(1*(im<128))
labels, nbr_objects = measurements.label(im)
print(nbr_objects)

im = array(Image.open('Desktop/Binary.png').convert('L'))
im_open = (morphology.binary_opening(255 - im,ones((5,2)),iterations=3))
labels_open, nbr_objects_open = measurements.label(im_open)
print(nbr_objects_open)

figure()
gray()
imshow(labels)
show()

figure()
hist(labels.flatten(),127)
xlim(0,50)
ylim(0,2500)
show()


figure()
gray()
imshow(labels_open)
show()

figure()
hist(labels_open.flatten(),127)
xlim(0,50)
ylim(0,2000)
show()
