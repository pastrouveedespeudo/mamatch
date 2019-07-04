import cv2



def cherche_roue(image):
    im = cv2.imread(image, 0)
    for x in range(im.shape[0]):
        for y in range(im.shape[1]):
            pass

    cv2.imshow('image.jpg', im)

cherche_roue('roue_nb.png')
