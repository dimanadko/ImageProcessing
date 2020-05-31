import math,numpy
import scipy.misc
from PIL import Image

a = Image.open('images/lena.png')
b = numpy.asarray(a)
gamma = 0.5

b1 =  b.astype(float)
b3 = numpy.max(b1)

b2 = b1/b3

b3 = numpy.log(b2)*gamma
c = numpy.exp(b3)*255.0

c1 = c.astype(int)
d = Image.fromarray(c1)
d.show()