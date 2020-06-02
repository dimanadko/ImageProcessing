from PIL import Image
from pylab import *

inputImage = array(Image.open('images/baboon.png').convert('L'))
gray()
negativeImage = 255 - inputImage
limitedRangeImage = 100.0 * inputImage/255 + 100
darkenedImage = 255.0 *(inputImage/255.0)**2

subplot(3,4,1)
plt.imshow(inputImage)
plt.title('Original')

subplot(3,4,2)
plt.imshow(negativeImage)
plt.title('Negative')

subplot(3,4,3)
plt.imshow(limitedRangeImage)
plt.title('Limited Range 100-200')

subplot(3,4,4)
plt.imshow(darkenedImage)
plt.title('Darkened with square function')

plt.show()
