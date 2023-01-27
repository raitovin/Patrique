import numpy
import matplotlib.pyplot as plt
from PIL import Image
import os


backgroundcolor = (255, 255, 255)
color = ()

img = Image.open("images/test2.png")
img_pxl = numpy.array(img)

#efface la couleur sélectionner
for i in range(int(img_pxl.shape[0])):
    for y in range(int(img_pxl.shape[1])):
        print("processing pixels " + str(i) + "|" + str(y))
        r,v,b = img.getpixel((i,y))

        #classe toute les couleurs présentes sur l'image
        if (r,v,b) != backgroundcolor:
            color += (r,v,b)

        """#couleur à effacer
        if img.getpixel((i, y)) == (0, 0, 0):
            img.putpixel((i, y), (255, 255, 255))"""

#remplace la couleur choisie par la couleur de l'arrière plan
for i in len(color):
    if color[i] == (0, 0, 0):
        img.getpixel(backgroundcolor)
            

print(type(img_pxl.shape))
print(img_pxl.flatten())

os.remove('output.png') #pensez à déplacer le fichier si vous voulez sauvegarder le rendu précédent
plt.imsave('output.png', numpy.array(img))

img.show()