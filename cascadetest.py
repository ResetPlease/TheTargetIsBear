import numpy as np
import cv2
from matplotlib import pyplot as plt


cas = cv2.CascadeClassifier('/home/beregom/Projects/The target is bears/data/cascade.xml')

img = cv2.imread("/home/beregom/Projects/The target is bears/TEST IMAGES/withBears/bb/5.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
bears = cas.detectMultiScale(gray, 50, 50)

# for (x,y,w,h) in bears:
#         cv2.rectangle(img,(x,y),(x+w+100,y+h+100),(255,255,0),2)

plt.imshow(img)
plt.show()


