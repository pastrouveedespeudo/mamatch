import cv2
from PIL import Image
import shutil


def resize(image, save):
    image = Image.open(image)
    image.resize((200,200)).save(save)
    

def crop(image, a, b, c, d):
    im = Image.open(image)
    im = im.crop((a, b, c, d))
    im.save('_0.png')
    #im.show()

def lecture_noir_blanc(image, save):

    oInput = input('ou ?')

    if oInput == 'o':
        path = r"C:\Users\jeanbaptiste\Desktop\onebyone\origine"
    else:
        path = r"C:\Users\jeanbaptiste\Desktop\onebyone\compa"

    im = cv2.imread(image, 0)

    for x in range(im.shape[0]):
        for y in range(im.shape[1]):
            if im[x,y] < 125:
                im[x,y] = 0
            else:
                im[x,y] = 255
                
    
    cv2.imshow('image.png', im)
    cv2.imwrite(save, im)
    shutil.move(save, path)



def matrice(image):

    matrice = []
    x_axe = []
    
    im = cv2.imread(image, 0)

    compteur = 0
    
    for x in range(im.shape[0]):
        for y in range(im.shape[1]):
            
            if x > compteur:
                matrice.append(x_axe)
                x_axe = []
                compteur += 1


            x_axe.append(im[x,y])

                
    return matrice


def comparaison_neg(image1, image2):
    liste = []
    
    
    mat = matrice(image1)
    mat2 = matrice(image2)
    

    c = 0
    diff = 0
    for i in mat:
        try:
            if i != mat2[c]:
                diff += 1
        except:
            c = 0
            
        c += 1


    print(diff)



def comparaison_pos(image1, image2):
    liste = []
    
    mat1 = matrice(image1)
    mat2 = matrice(image2)



    for i in mat1:
        for j in mat2:
            c = 0
            for ii in i:
                for jj in j:
                    if ii == jj:
                        c += 1
            if c == len(j):
                print(i,j)
                print('ouiiiiiiiiiiiiiiii')
 
        
 



#resize('voiture.png', 'voiture_resize2.png')
#du coup faut aussi resize la roue...

    
#lecture_noir_blanc('voiture_resize1.png', 'noir_blanc.png')
#comparaison_neg('noir_blanc.png', 'noir_blanc.png')
#lecture_noir_blanc('roue.jpg', 'roue_nb.png')

#crop('voiture_resize2.png', 90,120, 150, 180)
    
comparaison_pos('voiture_resize2.png', '_0.png')

































