import cv2
import numpy as np
import matplotlib.pyplot as plt
import random 

#read image
oimg = cv2.imread('Mona_Lisa_GS2.jpg',cv2.IMREAD_GRAYSCALE)
img = cv2.imread('Mona_Lisa_GS2.jpg', cv2.IMREAD_GRAYSCALE)
a,b = img.shape

# #randomly insert 0 and 1 as noise
# for i in range(0,a):
#     for j in range(0,b):
#         if random.random() < 0.1: 
#             img[i,j]=0
#         if random.random() > 0.9:
#             img[i,j]=255
# noise_img = img

#padding
img=np.pad(img,1,mode='symmetric')
print(img)


#sobel filter
sobel=[[-1,-2,-1],[0,0,0],[1,2,1]]
sobel2=[[-1,0,1],[-2,0,2],[-1,0,1]]
sobel=np.array(sobel)
sobel2=np.array(sobel2)
filtered_img = np.zeros((a,b))
filtered_img2 = np.zeros((a,b))
for i in range(1,a+1):
    for j in range(1,b+1):
        filtered_img[i-1,j-1]=np.sum(sobel*img[i-1:i+2,j-1:j+2])
        filtered_img2[i-1,j-1]=np.sum(sobel2*img[i-1:i+2,j-1:j+2])

resultimg=np.zeros((a,b))
for i in range(a):
    for j in range(b):
        resultimg[i][j]=int(abs(filtered_img[i][j]))+int(abs(filtered_img2[i][j]))
# Display images
plt.subplot(1, 4, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 4, 2)
plt.imshow(filtered_img, cmap='gray')
plt.title('X-axis Derivative')

plt.subplot(1, 4, 3)
plt.imshow(filtered_img2, cmap='gray')
plt.title('Y-axis Derivative')

plt.subplot(1, 4, 4)
plt.imshow(resultimg, cmap='gray')
plt.title('Filtered Image')

plt.show()






