import cv2
from PIL import Image
import shutil



liste = []
liste1 = []
im = cv2.imread('essais.jpg', 0)
for x in range(im.shape[0]):
    liste = []
    for y in range(im.shape[1]):
        
        if im[x,y] == 0:
            im[x,y] = 0
        else:
            im[x,y] = 255
            
        liste.append(im[x,y])

    liste1.append(liste)
cv2.imshow("image", im)
cv2.imwrite('essais2.jpg', im)






im = cv2.imread('essais2.jpg')

cv2.imshow("image", im)

liste2 = []

for i in liste1:
    c = 0
    for j in i:
        if j == 255:
            i[c] = 1
        elif j == 0:
            i[c] = 0
        c+=1
        
print(liste1)

l = 0
c = 0

carre = []

for i in liste1:
    l += 1
    c = 0
    for j in i:
        c += 1
        if j == 0:
            carre.append([l, c])
print('\n')
print(carre)
print('\n')
print('\n')


li = []
for i in carre:
    try:
        li.append(i[0])
        c+=1
    except:
        pass


yo = []
c = 0
a = []
num = min(li)
for i in carre:

    try:
        if carre[c+1][0] == carre[c][0]:
            a.append(carre[c])
        
    except:
        pass


    c+=1
    try:
        if carre[c][0] > num:
            num += 1
            yo.append(a)
            a = []
    except:
        pass



mean = []
c = 0
for i in yo:
    mean.append(len(i))

print(mean)
for i in mean:
    if i <= 1:
        mean.remove(i)

print(mean)


















