import cv2
from colour import *
import numpy as np
font = cv2.FONT_HERSHEY_COMPLEX

from couleur.coul import *



PATH = r'C:\Users\jeanbaptiste\Desktop\onebyone\couleur\bobo.txt'


def lecture(image):
    im = cv2.imread(image, 0)
    th = cv2.adaptiveThreshold(im,
                               255,
                               cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY, 115, 1)
    blur = cv2.medianBlur(th,15)

    cv2.imshow('image', blur)
    cv2.imwrite('traitement.jpg', blur)



def epparpillation(image):
    for x in range(im.shape[0]):
        for y in range(im.shape[1]):







def couleur():
    
    colordb = get_colordb(PATH)
    nearest = colordb.nearest(47, 79, 79)
    print(nearest)











if __name__ == '__main__':

    PATH_OEIL = r"C:\Users\jeanbaptiste\Desktop\onebyone\oeil\oeil3.jpg"

    lecture(PATH_OEIL)
    
























