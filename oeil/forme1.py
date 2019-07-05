import cv2
import numpy as np
font = cv2.FONT_HERSHEY_COMPLEX





PATH = r'C:\Users\jeanbaptiste\Desktop\onebyone\couleur\bobo.txt'


def lecture(image):
    
    im = cv2.imread(image, 0)
    th = cv2.adaptiveThreshold(im,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 115, 1)
    blur = cv2.medianBlur(th,15)

    cv2.imwrite('traitement.jpg', blur)





def lecture_noir_blanc(image):
    
    im = cv2.imread(image, 0)
    im2 = cv2.imread('redessinage.jpg', 0)

    for x in range(im.shape[0]):
        for y in range(im.shape[1]):
            if im[x,y] < 125:
                im2[x,y] = 255
            else:
                im2[x,y] = 0
                
    cv2.imwrite('redessinage.jpg', im2)





 

def fonction_cercle(x, x1, y, y1, r, longueur):
    r = 10
    
    pts = ((x - x0)**2) + ((y - y0)**2)
    
    

ROND = []
LISTE_EPAR = []
def eparpillation(image):

    les_rond = []
    
    im = cv2.imread(image)

    longueur = im.shape[0]

    for x in range(im.shape[0]):
        for y in range(im.shape[1]):

            r = 5
            
            Ocontinuer = True
            while Ocontinuer:
                print(r)
                rond = cv2.circle(im, (20, 20), r, (False), 1)
                diametre = len(rond)
                pts = 0
                les_rond.append([x,y,r])
                compt = 0
                for i in rond:
                    for j in i:
                        compt += 1
                        if j[0] == 255 and j[1] == 255 and j[2] == 255:
                            pts += 1
                            
                print(compt, pts)
                if pts == compt:
                    Ocontinuer = True
                    les_rond = []
                    pts = 0
                    r += 5

                elif pts != diametre:
                    ROND.append(les_rond)
                    Ocontinuer = False

  
                cv2.imshow('image', im)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                






        











if __name__ == '__main__':

    PATH_OEIL = r"C:\Users\jeanbaptiste\Desktop\onebyone\oeil\oeil1.jpg"

    lecture(PATH_OEIL)
    lecture_noir_blanc('traitement.jpg')
    liste, longueur = eparpillation('redessinage.jpg')
    cherche(liste, longueur)
























