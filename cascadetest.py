import numpy as np
import cv2
from matplotlib import pyplot as plt


cas = cv2.CascadeClassifier('/home/beregom/Projects/The target is bears(v0.001)/data/cascade.xml')

img = cv2.imread("TEST IMAGES/withBears/bb/5.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
bears = cas.detectMultiScale(gray, 50, 50)

plt.imshow(img)
plt.show()


