import cv2
import numpy as np
import matplotlib.pyplot as plt
import random 

#read image
oimg = cv2.imread('OIG3 (1).jpg',cv2.IMREAD_GRAYSCALE)
img = cv2.imread('OIG3 (1).jpg', cv2.IMREAD_GRAYSCALE)
a,b = img.shape


#gaussian noise
img=img+np.random.normal(0,20,(a,b))
img=np.clip(img,0,255)
noise_img = img


#padding
img=np.pad(img,1,mode='symmetric')
print(img)

#filter mask
mask = np.array([[1,1,1],[1,1,1],[1,1,1]])
#apply to each pixel of orginal image
for i in range(1,a+1):
    for j in range(1,b+1):
        img[i,j]=(np.sum(mask*img[i-1:i+2,j-1:j+2]))/9
filtered_img = img[1:a+1,1:b+1]
print(img[1:a+1,1:b+1]) 
# Display images
plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.imshow(oimg, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 3, 2)
plt.imshow(noise_img, cmap='gray')
plt.title('Noisy Image')

plt.subplot(1, 3, 3)
plt.imshow(filtered_img, cmap='gray')
plt.title('Filtered Image')

plt.show()



