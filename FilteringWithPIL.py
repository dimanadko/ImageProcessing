from PIL import Image
from PIL import ImageFilter
from pylab import *



class ShowFilteredImage():
    counter=1
    im=None
    figure(figsize=(15, 15))
    def __init__(self, inputImage):
        self.im = inputImage
        subplot(3, 4, 1)
        plt.imshow(self.im)
        plt.title('Original')

    def addPicture(self, customFilter, title):
        subplot(3, 4, self.counter)
        plt.imshow(self.im.filter(customFilter))
        plt.title(title)
        self.counter = self.counter+1
    def show(self):
        plt.show()

im0 = Image.open('images/baboon.png')
# figure(figsize =(15,15))

FilterableImage  = ShowFilteredImage(im0)
FilterableImage.addPicture(ImageFilter.CONTOUR, 'Contour')
FilterableImage.addPicture(ImageFilter.DETAIL, 'Detail')
FilterableImage.addPicture(ImageFilter.EDGE_ENHANCE, 'Edge Enhance')
FilterableImage.addPicture(ImageFilter.EDGE_ENHANCE_MORE, 'Edge Enhance More')
FilterableImage.addPicture(ImageFilter.EMBOSS, 'Emboss')
FilterableImage.addPicture(ImageFilter.FIND_EDGES, 'Find Edges')
FilterableImage.addPicture(ImageFilter.SMOOTH, 'Lowpass 1')
FilterableImage.addPicture(ImageFilter.SMOOTH_MORE, 'Lowpass 2')
FilterableImage.addPicture(ImageFilter.SHARPEN, 'Sharpen')

size = (3,3)
kernel1  = [1,1,1,1,-1,1,-1,-1,-1]
ker1 =  ImageFilter.Kernel(size,kernel1,scale=None,offset =0)
FilterableImage.addPicture(ker1, 'Custom Filter 1')


kernel2 = [1,0,-1,1,0,-1,0,0,-1]
ker2 = ImageFilter.Kernel(size,kernel2,scale =None,offset=0)
FilterableImage.addPicture(ker2, 'Custom Filter 2')

FilterableImage.show()