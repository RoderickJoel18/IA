from PIL import Image 
import glob
import time 

img1 = "C:/Users/roder/OneDrive/Documentos/Programación/Python/Basicos/IA/app_img/Imagenes/1.jpeg"
img2 = "C:/Users/roder/OneDrive/Documentos/Programación/Python/Basicos/IA/app_img/Imagenes/2.jpeg"
img3 = "C:/Users/roder/OneDrive/Documentos/Programación/Python/Basicos/IA/app_img/Imagenes/3.jpeg"
img4 = "C:/Users/roder/OneDrive/Documentos/Programación/Python/Basicos/IA/app_img/Imagenes/4.jpeg"
img5 = "C:/Users/roder/OneDrive/Documentos/Programación/Python/Basicos/IA/app_img/Imagenes/5.jpeg"
suma = len(glob.glob("C:/Users/roder/OneDrive/Documentos/Programación/Python/Basicos/IA/app_img/Imagenes/*.jpeg"))

imagenes = [img1, img2, img3, img4, img5]
for i in imagenes:
    img = Image.open(i)
    img.show()
    time.sleep(3)

print("La sumatoria de imagenes es: "+ str(suma))