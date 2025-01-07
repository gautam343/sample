import numpy as np
import cv2

def padding(image, pad_width):
    height,width = image.shape
    new_height = height + 2 * pad_width
    new_width = width + 2 * pad_width

    result_image = np.zeros((new_height, new_width), dtype=image.dtype)

    result_image[pad_width:new_height - pad_width, pad_width:new_width - pad_width] = image

    return result_image

def apply_mask(image, mask):
    pad_width = mask.shape[0] // 2
    padded_image = padding(image,pad_width)
    result_image = np.zeros_like(image, dtype = np.float32)

    for i in range(pad_width, len(padded_image) - pad_width):
        for j in range(pad_width, len(padded_image[0]) - pad_width):
            window = padded_image[i - pad_width:i + pad_width + 1, j - pad_width:j + pad_width + 1]
            result_image[i - pad_width, j - pad_width] = round(np.sum(window * mask))

    return result_image

image = cv2.imread("Mona_Lisa_GS2.jpg", cv2.IMREAD_GRAYSCALE)

mask1 = np.array([[-1,-1,-1],
                    [0,0,0],
                    [1,1,1]])

mask2 = np.array([[-1,0,1],
                    [-1,0,1],
                    [-1,0,1]])


gx = apply_mask(image,mask1)
gy = apply_mask(image,mask2)

result_image = np.zeros((image.shape[0], image.shape[1]),dtype=int)

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        result_image[i,j] = int(abs(gx[i,j])) + int(abs(gy[i,j]))


sobel_x = cv2.Sobel(image, cv2.CV_32F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_32F, 0, 1, ksize=3)
        

import matplotlib.pyplot as plt
plt.subplot(2, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

plt.subplot(2, 3, 2) 
plt.imshow(gx, cmap='gray')
plt.title('X-axis Derivative')

plt.subplot(2, 3, 3)
plt.imshow(gy, cmap='gray')
plt.title('Y-axis Derivative')

plt.subplot(2,3,4)
plt.imshow(result_image, cmap='gray')
plt.title("Result Image")

plt.subplot(2,3,5)
plt.imshow(sobel_x, cmap='gray')
plt.title("Sobel X")

plt.subplot(2,3,6)
plt.imshow(sobel_y, cmap='gray')
plt.title("Sobel Y")
plt.show()