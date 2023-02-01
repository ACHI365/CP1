import cv2 as cv
import numpy as np


# somewhat same style as cv.addWeight
def add(img1, img2, alpha, length, width):
    res = np.zeros((length, width, 3))
    for row in range(length):
        for column in range(width):
            pixel1 = img1[row][column]
            pixel2 = img2[row][column]
            res[row][column] = pixel1 * alpha + pixel2 * (1 - alpha)  # adds pixels based on its weight
    return res


# for weight measurement
alpha = 0

# take images as matrices
img1 = cv.imread('img/basketball1.png')
img2 = cv.imread('img/Blender_Suzanne1.jpg')

# for images with different sizes
length = min(img1.shape[0], img2.shape[0])
width = min(img1.shape[1], img2.shape[1])

while alpha < 1:
    res = add(img1, img2, alpha, length, width)
    cv.imshow("video", res.astype(np.uint8))  # slowly add alpha meter and make an effect of video
    alpha += 0.1
    cv.waitKey(1000)
