import numpy
import matplotlib.pyplot as plt
from PIL import Image
import os
import cv2
import colorsys

def rgb_to_hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = (df/mx)*100
    v = mx*100
    return h, s, v

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


hsv = cv2.cvtColor(img_, cv2.COLOR_BGR2HSV)

mask1 = cv2.inRange(hsv, (0, 50, 20), (370, 370, 370))
mask2 = cv2.inRange(hsv, (175, 50, 50), (180, 255, 255))

mask = cv2.bitwise_or(mask1, mask2)

for i in range(len(color)):
    if color[i] != (0,0,0):
        r, g, b = color[i]
        
        (h, s, v) = rgb_to_hsv(r, g, b)
        gilbert = (int(h), int(s), int(v))
        print(gilbert)
        #bleu
        if gilbert >= (100, 50, 20) and gilbert <= (140, 255, 255):
            p_color = (color[i])
            print('bleu')
            contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            break
        elif gilbert >= (169, 20, 74) and gilbert <= (255, 255, 255):
            p_color = (color[i])
            print('bleu')
            contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            break
        #vert
        if gilbert >= (40, 50, 20) and gilbert <= (136, 255, 255):
            p_color = (color[i])
            print('vert')
            contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            break
        #red
        if gilbert >= (0, 50, 20) and gilbert <= (5, 255, 255) or gilbert >= (350, 50, 0):
            p_color = (color[i])
            print('rouge')
            contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            break


for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    print(p_color) 
    cv2.rectangle(img_, (x, y), (x+ w, y + h), p_color, -1)


#enregistre le résultat
try:
    os.remove('temp.png')
    os.remove('output.png') #pensez à déplacer le fichier si vous voulez sauvegarder le rendu précédent
except:
    print("pas de fichier output préalablement créé")

plt.imsave('output.png', numpy.array(img_))
#img.show()
