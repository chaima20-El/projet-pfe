import cv2
import numpy as np 

img = cv2.imread('lena_bruit_gaussien_alpha.jpg',0)
new_img = cv2.imread('lena_bruit_gaussien_alpha.jpg', 0)
#print(shape)
prop = img.shape
print('Image Height       : ',prop)
print('Image Width        : ',prop[1])
#print('rang                :',range(prop[0],prop[0]-1))

############### 3x3 window ############### 
for i in range(1, prop[0] - 1):# pour toutes les lignes i de l’image


    for j in range(1, prop[1] - 1):
        
        win = []
        
        for x in range(i-1, i + 2):
            for y in range(j-1, j+2):
                win.append( img[x][y] )
        #sort the values
        win.sort()

        new_img[i][j] = win[4]#median
        

cv2.imwrite('3x3median_gauss_alpha.jpg', new_img )


############### 5x5 window ###############
new_img = cv2.imread('lena_bruit_gaussien_alpha.jpg', 0)

for i in range(1, prop[0] - 2):
    for j in range(1, prop[1] - 2):
        win = []
        for x in range(i - 2, i + 3):
            for y in range(j - 2, j + 3):
                win.append(img[x][y])
        #sort the values
        win.sort()

        new_img[i][j] = win[12]

cv2.imwrite('5x5median_gauss_alpha.jpg', new_img)
