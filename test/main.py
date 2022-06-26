Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import cv2 as cv
import numpy as np 

def imageSize(img):    
    require_size = 10000000
    size = img.size

    if size < require_size: 
        print("The image size is validated")
    else: 
        print('The size of the image is Invalid')


def getImageType(img):
    dataType = img.dtype
    print("The image data type is: ", dataType)

    imageSize(img)


def dimentionValidation(img):
    size = img.shape

    x = 900
    y = 900

    if size[0] > x and size[1] > y: 
        print("Image dimension is not valid")
    else: 
        print("Image dimension is cleared")

    getImageType(img)

def accesspx(img):
   x = int(input("Enter the x coordinate: "))
   y = int(input("Enter the y coordinate: "))
   c = int(input("Enter the attribute color 0 Blue 1 Green 2 Red: "))
   
   px = img.item(x,y,c)
   print("Pixel value: ", px)

   img.itemset((x, y, c), 100)
   px = img.item(x,y,c)
   print("After modify: ", px)
   
   dimentionValidation(img)



def loadImage():
    img = cv.imread('./test/nikolai.jpg')


    img_p = img.shape
    if len(img_p) != 3: 
        print("Grayscale image is not allowed")
    else : 
        accesspx(img)



loadImage()