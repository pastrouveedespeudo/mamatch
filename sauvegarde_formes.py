import cv2
from PIL import Image
import shutil



liste = []
liste1 = []
im = cv2.imread('b.jpg', 0)
for x in range(im.shape[0]):
    liste = []
    for y in range(im.shape[1]):
        
        if im[x,y] < 125:
            im[x,y] = 255
        else:
            im[x,y] = 0
            
        liste.append(im[x,y])

    liste1.append(liste)

cv2.imshow("oinoi", im)


print(liste1)


































