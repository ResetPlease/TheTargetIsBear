import cv2
import random
import os

def rotate_image(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result


info = open("info/info.lst","w+")

# back = cv2.imread("neg/1.jpg")
# front = cv2.imread("target/1.jpg")

targetpath = "/home/beregom/Projects/The target is bears/target/"
negpath = "/home/beregom/Projects/The target is bears/neg/"
target = os.listdir(targetpath)
neg = os.listdir(negpath)

for i in range(5):
    x_offset=random.randint(400,7300)
    y_offset=random.randint(400,7300)
    back = cv2.imread(negpath+neg[random.randint(0,len(neg)-1)])
    front = cv2.imread(targetpath+target[random.randint(0,len(target)-1)])
    back[y_offset:y_offset+front.shape[0], x_offset:x_offset+front.shape[1]] = front
    name = "0"*(4-len(str(i)))+str(i)+"_"+"0"*(4-len(str(x_offset)))+str(x_offset)+"_"+"0"*(4-len(str(y_offset)))+str(y_offset)+"_"+"0"*(4-len(str(front.shape[0])))+str(front.shape[0])
    name = name +"_"+"0"*(4-len(str(front.shape[1])))+str(front.shape[1])
    cv2.imwrite("info/"+name+".jpg",back)

info.close()