import numpy
import matplotlib.pyplot as plt
from PIL import Image
import os
import cv2
import colorsys

"""
                            /!\ IMPORTANT /!\


cette verion ne fonctionne qu'avec des RECTANGLES de couleurs ROUGE et NOIR
"""

#def replacer(w, h):

backgroundcolor = (255, 255, 255)
color = []
pixel_coor = []

coor = []

img = Image.open("images/test4.png")

#efface la couleur sélectionner
for i in range(img.width):
    for y in range(img.height):
        #print("checking pixels " + str(i) + "|" + str(y))
        r,v,b = img.getpixel((i,y))
        r_,v_,b_ = img.getpixel((i-1,y))

        #classe toute les couleurs présentes sur l'image
        if (r,v,b) != backgroundcolor:
            

            color.append((r,v,b))
            pixel_coor.append((i,y))

        """#couleur à effacer
        if img.getpixel((i, y)) == (0, 0, 0):
            img.putpixel((i, y), (255, 255, 255))"""

#remplace la couleur choisie par la couleur de l'arrière plan
for i in range(len(color)):
    if color[i] == (0, 0, 0):
        #print("replacing pixels " + str(i) + "/" + str(len(color)))
        img.putpixel(pixel_coor[i],backgroundcolor)

#créer une image temporaire
plt.imsave('temp.png', numpy.array(img))

#refait la forme si celle ci n'était pas complete
img_pxl = numpy.array(img)
img_ = cv2.imread('temp.png')

#si plusieurs shape couleur sélectioné pour disparaître

p_color = (0, 0, 0)

blue = [(0, 0, 10), (0, 0, 255)]
green = [(0, 10, 0), (0, 255, 0)]
red = [(10, 0, 10), (255, 0, 0)]

for i in range(len(color)):
    if color[i] != (0,0,0):
        r, g, b = color[i]
        r, g, b = r/255, g/255, b/255
        (h, s, v) = colorsys.rgb_to_hsv(r, g, b)
        (h, s, v) = (int(h * 179), int(s * 255), int(v * 255))
        gilbert = (h, s, v)
        print((h, s, v))
        #bleu
        if gilbert >= (100, 50, 20) and gilbert <= (140, 255, 255):
            p_color = (color[i])
            
            break


hsv = cv2.cvtColor(img_, cv2.COLOR_BGR2HSV)

mask1_red = cv2.inRange(hsv, (0, 50, 20), (5, 255, 255))
mask2_red = cv2.inRange(hsv, (175, 50, 50), (180, 255, 255))

mask1_blue = cv2.inRange(hsv, (100, 50, 20), (140, 255, 255))
mask2_blue = cv2.inRange(hsv, (175, 50, 50), (180, 255, 255))

mask1_green = cv2.inRange(hsv, (40, 50, 50), (80, 255, 255))
mask2_green = cv2.inRange(hsv, (175, 50, 50), (180, 255, 255))

def mask(mask1, mask2):
    
    mask = cv2.bitwise_or(mask1, mask2)
    return mask

contours, _ = cv2.findContours(mask(mask1_blue, mask2_blue), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
     x, y, w, h = cv2.boundingRect(contour)

     cv2.rectangle(img_, (x, y), (x+ w, y + h), p_color, -1)


#enregistre le résultat
try:
    os.remove('temp.png')
    os.remove('output.png') #pensez à déplacer le fichier si vous voulez sauvegarder le rendu précédent
except:
    print("pas de fichier output préalablement créé")

plt.imsave('output.png', numpy.array(img_))
#img.show()
