import cv2
from matplotlib import pyplot as plt

img = cv2.imread('images/baboon.png')

output = cv2.Laplacian(img,-1)

plt.imshow(output)
plt.show()
