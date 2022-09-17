import cv2 # pip install opencv-python
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter
import filesOutIn



def main():

    imageFolder = 'C:\\Develop\\Python\\TestRozpoznejFoto\Test1\\fotoElm\\'
    output_path = 'C:\\Develop\\Python\\TestRozpoznejFoto\\Test1\\outputDisplay\\'
    listImage = filesOutIn.getAllFilesFromFolder(imageFolder)

    for fileImg in listImage:

        image_name_out= output_path + fileImg #"ciselnik2_" + str("al") + ".jpg"
        image_path = imageFolder + fileImg
        img = cv2.imread(image_path)
        imgOrig = cv2.imread(image_path)
        img = blurImage(img)
        #img = userContrast(img)
        imgMask = userMask(imgOrig,img)
        cutOut = getMaxEdge(imgMask, imgOrig)

        if 1<0:
            cv2.imshow('Image',img)
            cv2.imshow('Image mask',imgMask)
            cv2.imshow('vyrez',cutOut)
            cv2.waitKey(0)

        cv2.imwrite(image_name_out,cutOut)
        print("ukladam")






#rozostření obrázku
def blurImage(img):
    img_blur = cv2.GaussianBlur(img, (11, 11), 2)
    return img_blur

#zvíraznění barvy
def userContrast(img):

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    greenMask = cv2.inRange(hsv, (26, 10, 30), (97, 100, 255))
    img[greenMask == 255] = (0, 255, 0)
    hsv[:,:,1] = greenMask 
    back = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    return back


#maska obrázku
def userMask(imgOrig, img):

    low_green = (20, 115, 15)#(20, 115, 15)tmavě zelená
    high_green = (140, 255,218)# (140, 255,230) # 24,158,17


    #low_green = (37, 21, 0)#(20, 115, 15)tmavě zelená
    #high_green = (74, 228,255)# (140, 255,230) # 24,158,17
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)       
    mask = cv2.inRange(hsv, low_green , high_green)


    result = cv2.bitwise_and(imgOrig,imgOrig, mask=mask)
    greenMask = cv2.GaussianBlur(result, (5, 5), 1)

    #cv2.imshow('img greenMask', greenMask)
    #cv2.waitKey(0)

    return greenMask

#vrátí výřez obrázku podle nejdelší hrany
def getMaxEdge(imgMask,imgOrig):

    tLower = 125  # nizky prahLower Threshold
    tUpper = 200 # vysoky prah Upper threshol
    L2Gradient = True
    edges = cv2.Canny(imgMask, tLower, tUpper, L2gradient = L2Gradient )#detekce hran
    #cv2.imshow('img edges', edges )
    #cv2.waitKey(0)
 
    #cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours, hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    contour = max(contours, key = len)
    #contourImg = cv2.drawContours(imgOrig, contour, -1, (0,255,0), 2)#pokud chceme zobrazit kontury
    #cv2.imshow("Contours", contourImg)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    #sorted_contours= sorted(contours, key=cv2.contourArea, reverse= True)
    x,y,w,h= cv2.boundingRect(contour)#nakreslím obdelník v nalezené max kontuře

    cropped_contour= imgOrig[y:y+h, x:x+w]
    #cv2.imshow("Contours", cropped_contour)
    #cv2.waitKey(0)

    return cropped_contour



main()