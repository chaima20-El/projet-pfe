
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
#path=r"C:/Users/chaimaelmejgari/Desktop/py/lena.png"
image = cv.imread(r"c:/Users/chaimaelmejgari/Desktop/py/lena_bruit_gaussien_alpha.jpg")

image = cv.cvtColor(image, code=cv.COLOR_BGR2RGB)
#dst =cv.fastNlMeansDenoising(image, None, 65, 5, 21)

dst = cv.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)
# dst2=cv.cvtColor(dst,code=cv.COLOR_BGR2RGB)

plt.subplot(121), plt.imshow(image)
plt.subplot(122), plt.imshow(dst)
# plt.subplot(122), plt.imshow(dst2)
plt.show()
cv.imwrite('nlmeans1_gauus_alpha.jpg',dst)
cv.imwrite('nlmeans2_gauus_alpha.jpg',image)
