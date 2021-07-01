#подключаем необходимые библиотеки
import cv2
import numpy as np
from matplotlib import pyplot as plt
from numpy.core.fromnumeric import resize

#примеры 2х картинок на которых всё работает хорошо
#img = cv2.imread("TEST IMAGES/withBears/_2016-04-25 13-50-46_1257_R.JPG")
#img = cv2.imread("TEST IMAGES/withBears/2016-05-13 11-33-21_0855_2R.JPG")
#img = cv2.imread("TEST IMAGES/withBears/2016-04-25 13-59-31_1410_R.JPG")


img = cv2.imread("TEST IMAGES/withBears/2016-04-25 13-59-31_1410_R.JPG")

img_RGB=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV_FULL)
#цвет медведя, но это не точно 
light_orange = (24, 50, 49)
dark_orange = (280, 82, 73)
mask = cv2.inRange(img_hsv, light_orange, dark_orange)
grayImage = cv2.cvtColor(img_RGB, cv2.COLOR_RGB2GRAY)
grayImage = cv2.cvtColor(grayImage,cv2.COLOR_GRAY2RGB)
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 150, 255, cv2.THRESH_BINARY)
# plt.imshow(mask)
# plt.show()
plt.imshow(grayImage)
plt.show()
# plt.imshow(blackAndWhiteImage)
# plt.show()

# #находим точку на картинке которая максимально похоже по цвету на медведя

# position = np.unravel_index(np.argmax(mask), mask.shape)
# print(position)
# print(mask[0][0])

# #выризаеим картинку чтобы посмотреть
# y=position[0]-100
# x=position[1]-100
# h=200
# w=200
# crop = img_RGB[y:y+h, x:x+w]
# plt.imshow(crop)
# plt.show()

# # выделяем медведя на общей картинке
# cv2.rectangle(img_RGB, (x,y), (x+w,y+h), (0, 255, 255), 20)
# plt.imshow(img_RGB)
# plt.show()