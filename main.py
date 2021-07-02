#подключаем необходимые библиотеки
import cv2
import numpy as np
from matplotlib import pyplot as plt
from numpy.core.fromnumeric import resize
import sys
import os

class HSV:
    mn = ()
    mx = ()
    def __init__(self,h1,s1,v1,h2,s2,v2) -> None:
        self.mn = (h1,s1,v1)
        self.mx = (h2,s2,v2)


def drawbestconturs(mask, img):
    try:
        areaArray = []
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for i, c in enumerate(contours):
            area = cv2.contourArea(c)
            areaArray.append(area)

        sorteddata = sorted(zip(areaArray, contours), key=lambda x: x[0], reverse=True)
        return sorteddata
        # secondlargestcontour = sorteddata[-1][1]
        # x, y, w, h = cv2.boundingRect(secondlargestcontour)
        # return x, y, w, h
    except:
        return -1



#img = cv2.imread("TEST IMAGES/withBears/_2016-04-25 13-50-46_1257_R.JPG")
#img = cv2.imread("TEST IMAGES/withBears/2016-04-25 13-59-31_1410_R.JPG") --
#img = cv2.imread("/home/beregom/Projects/The target is bears(v0.001)/TEST IMAGES/withBears/bb/18.jpg")
#img = cv2.imread("TEST IMAGES/withBears/bb/5.jpg")
#img = cv2.imread("TEST IMAGES/withBears/bb/1.jpg")
#img = cv2.imread("TEST IMAGES/withBears/bb/7.jpg")
img = cv2.imread("TEST IMAGES/withBears/bb/8.jpg")

if(len(sys.argv) != 1 ):
    path = sys.argv[1]
    if(not os.path.exists(path)):
        print("Error: incorrect path")
        exit()
    img = cv2.imread(path)

plt.imshow(img)
plt.show()

v1 = HSV(15,0,0,52,29,89)
v2 = HSV(18,21,93,106,68,116)
v3 = HSV(0,0,0,82,12,137)
v4 = HSV(0,24,0,70,72,196)

img2 = img.copy()

img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

mask = cv2.inRange(img, v1.mn, v1.mx)
# plt.imshow(mask)
# plt.show()
sorteddata = drawbestconturs(mask, img)
for i in range(min(1,len(sorteddata))):
    x, y, w, h = cv2.boundingRect(sorteddata[i][1])
    cv2.rectangle(img2, (x, y), (x+w+100, y+h+100), (0,255,0), 5)


mask = cv2.inRange(img, v2.mn, v2.mx)
sorteddata = drawbestconturs(mask, img)
for i in range(min(1,len(sorteddata))):
    x, y, w, h = cv2.boundingRect(sorteddata[i][1])
    cv2.rectangle(img2, (x, y), (x+w+100, y+h+100), (0,255,0), 5)


mask = cv2.inRange(img, v3.mn, v3.mx)
sorteddata = drawbestconturs(mask, img)
for i in range(min(1,len(sorteddata))):
    x, y, w, h = cv2.boundingRect(sorteddata[i][1])
    cv2.rectangle(img2, (x, y), (x+w+100, y+h+100), (0,255,0), 5)


mask = cv2.inRange(img, v4.mn, v4.mx)
sorteddata = drawbestconturs(mask, img)
for i in range(min(1,len(sorteddata))):
    x, y, w, h = cv2.boundingRect(sorteddata[i][1])
    cv2.rectangle(img2, (x, y), (x+w+100, y+h+100), (0,255,0), 5)


plt.imshow(img2)
plt.show()
