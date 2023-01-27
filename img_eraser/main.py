import numpy
import matplotlib.pyplot as plt
from PIL import Image

pxl_black = (0, 0, 0)
pxl_white = (255, 255, 255)

img = Image.open("images/test.png")
img_pxl = numpy.array(img)

for i in range(int(img_pxl.shape[0])):
    for y in range(int(img_pxl.shape[1])):
        
        if img.getpixel((i, y)) == (0, 0, 0):
            img.putpixel((i, y), (255, 255, 255))
            

print(type(img_pxl.shape))
print(img_pxl.flatten())

plt.imsave('output.png', numpy.array(img))

img.show()