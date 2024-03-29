import cv2
import numpy as np
font = cv2.FONT_HERSHEY_COMPLEX

def recog(image):
    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    _, threshold = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)
    contours,hierachy=cv2.findContours(threshold,
                                       cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        
        approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
        cv2.drawContours(img, [approx], 0, (0,0,255), 10)
        
        x = approx.ravel()[0]
        y = approx.ravel()[1]

        
        if len(approx) == 3:
            #cv2.putText(img, (x, y), font, 1, (0))
            print('Triangle')
            
        elif len(approx) == 4:
            #cv2.putText(img, "Rectangle", (x, y), font, 1, (0))
            print('Rectangle')
            
        elif len(approx) == 5:
            #cv2.putText(img, "Pentagon", (x, y), font, 1, (0))
            print('Pentagon')
            
        elif 6 < len(approx) < 15:
            cv2.putText(img, "Ellipse", (x, y), font, 1, (0))
            print('Ellipse')
            
        else:
            cv2.putText(img, "Circle", (x, y), font, 1, (0))
            print('Circle')



    cv2.imshow("shapes", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
