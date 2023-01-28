import numpy
import matplotlib.pyplot as plt
from PIL import Image
import os


backgroundcolor = (255, 255, 255)
color = []
pixel_coor = []

img = Image.open("images/test3.png")
img_pxl = numpy.array(img)

print(img_pxl.shape)
print(img_pxl.flatten())

#efface la couleur sélectionner
for i in range(img.width):
    for y in range(img.height):
        print("checking pixels " + str(i) + "|" + str(y))
        r,v,b = img.getpixel((i,y))

        #classe toute les couleurs présentes sur l'image
        if (r,v,b) != backgroundcolor:
            color.append((r,v,b))
            pixel_coor.append((i,y))

        """#couleur à effacer
        if img.getpixel((i, y)) == (0, 0, 0):
            img.putpixel((i, y), (255, 255, 255))"""


print(len(color))

#remplace la couleur choisie par la couleur de l'arrière plan
for i in range(len(color)):
    if color[i] == (0, 0, 0):
        print("replacing pixels " + str(i) + "/" + str(len(color)))
        img.putpixel(pixel_coor[i],backgroundcolor)
try:
    os.remove('output.png') #pensez à déplacer le fichier si vous voulez sauvegarder le rendu précédent
except:
    print("pas de fichier output préalablement créé")

plt.imsave('output.png', numpy.array(img))

#img.show()
