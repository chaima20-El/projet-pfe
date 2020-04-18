import numpy as np
import cv2
path =  'lena_bruit_gaussien_alpha.jpg'
img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
img_out = img.copy()

height = img.shape[0]
width = img.shape[1]

for i in np.arange(3, height-3):
    for j in np.arange(3, width-3):      
        max = 0
        for k in np.arange(-3, 4):
            for l in np.arange(-3, 4):
                a = img.item(i+k, j+l)
                if a > max:
                    max = a
        b = max
        img_out.itemset((i,j), b)

cv2.imwrite('max_gauss_alpha.jpg', img_out)

cv2.imshow('image',img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()