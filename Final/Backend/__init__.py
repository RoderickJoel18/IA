#Importación de paquetes a utiliozar 
import cv2
import imutils
import numpy as np
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
import re

#se carga la aimagen a utilozar
img = cv2.imread('Imagenes\c.jpg',cv2.IMREAD_COLOR)
img = cv2.resize(img, (620,480) )
#Se transforma la imagen a blanco y negro
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
#Extraer la información util de la imagen(La matrícula) 
gray = cv2.bilateralFilter(gray, 11, 17, 17) 
#Detección de bordes
edged = cv2.Canny(gray, 30, 200) 

#Se buscan los contornos de la imagen
cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
screenCnt = None

# loop over our contours
for c in cnts:
 # approximate the contour
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.018 * peri, True)
 
 # if our approximated contour has four points, then
 # we can assume that we have found our screen
    if len(approx) == 4:
        screenCnt = approx
        break

if screenCnt is None:
    detected = 0
    print ("No contour detected")
else:
    detected = 1

if detected == 1:
    cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 3)

# Masking the part other than the number plate
mask = np.zeros(gray.shape,np.uint8)
new_image = cv2.drawContours(mask,[screenCnt],0,255,-1,)
new_image = cv2.bitwise_and(img,img,mask=mask)
cv2.imshow('Matricula', new_image)
cv2.waitKey(0)

# Now crop
(x, y) = np.where(mask == 255)
(topx, topy) = (np.min(x), np.min(y))
(bottomx, bottomy) = (np.max(x), np.max(y))
Cropped = gray[topx:bottomx+1, topy:bottomy+1]
cv2.imshow('final', Cropped)
cv2.waitKey(0)

text = tess.image_to_string(Cropped, config='--psm 11')
print("Matrícula vehicular detectada: " + text)

patron1 = re.compile('([0-9]{6})')
patron2 = re.compile('([A-Z]{2}[0-9]{4})')
placa1 = patron1.findall(text)
placa2 = patron2.findall(text)
if patron1 is []:
    print ("La lista está vacia")
    if patron2 is not []:
        for i in placa2:
            valor = i
            print(i)

elif patron1 is not []: 
    for i in placa1:
        valor = i
        print(i)
