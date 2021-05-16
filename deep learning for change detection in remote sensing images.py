import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
 #creating data sets
DATADIR="C:/datasets/trainingdata"
CATEGORIES=['after','before']
#converting into greyscale
for category in CATEGORIES:
    path = os.path.join(DATADIR,category)
    for img in os.listdir(path):
        img_array=cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
        plt.imshow(img_array, cmap="gray")
        break
    plt.show()
    break
#counting the data in data sets
training_data =[]
def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR,category)
        class_num = CATEGORIES.index(category)
        for img in os.listdir(path):
            try:
                img_array=cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array,(120,120))
                plt.show()
                training_data.append([new_array, class_num])
            except Exception as e:
                print("Failed")
create_training_data()
print(len(training_data))
#getting image difference
from PIL import Image, ImageChops 
img1 = Image.open(r'C:\datasets\trainingdata\before\01.jpg') 
img2 = Image.open(r'C:\datasets\trainingdata\after\02.jpg')
diff = ImageChops.difference(img1, img2) 
diff.show() 
