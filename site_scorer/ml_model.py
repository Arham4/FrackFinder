import numpy as np
import cv2
from autokeras.image.image_supervised import ImageClassifier

num_images = 43

x_train = []
for i in range (1,num_images+1):
    img = cv2.imread("images/" + str(i) + ".jpg")
    resized_image = cv2.resize(img, (100,100))
    x_train.append(resized_image)
print(len(x_train))
x_train = np.array(x_train)

y_train = [i for i in range (1,num_images+1)] 

x_test = []
img = cv2.imread("images/" + str(num_images) + ".jpg")
resized_image = cv2.resize(img, (100,100))
x_test.append(resized_image)
x_test = x_test[0]
x_test = np.array(x_test)

y_test = [num_images]

x_train = x_train.reshape(x_train.shape + (1,))
x_test = x_test.reshape(x_test.shape + (1,))

clf = ImageClassifier(verbose=True)
clf.fit(x_train, y_train, time_limit=2 * 60)
clf.final_fit(x_train, y_train, x_test, y_test, retrain=True)
y = clf.evaluate(x_test, y_test)
print(y)
