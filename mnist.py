# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 15:42:39 2019

@author:Faith, Matthias, and Diana
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.datasets import fetch_mldata
from sklearn.datasets import get_data_home
from sklearn.model_selection import train_test_split
from shutil import copyfileobj
from six.moves import urllib
from sklearn.datasets.base import get_data_home
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.neural_network import MLPClassifier


#here's a function that downloads MNIST from another source and stores
# it in the default location where scikit-learn stores mldata datasets 
#(`~/scikit_learn_data/mldata/`). So after you call this function, 
#`fetch_mldata("MNIST original")` will work fine.

def fetch_mnist(data_home=None):
    mnist_alternative_url = "https://github.com/amplab/datascience-sp14/raw/master/lab7/mldata/mnist-original.mat"
    data_home = get_data_home(data_home=data_home)
    data_home = os.path.join(data_home, 'mldata')
    if not os.path.exists(data_home):
        os.makedirs(data_home)
    mnist_save_path = os.path.join(data_home, "mnist-original.mat")
    if not os.path.exists(mnist_save_path):
        mnist_url = urllib.request.urlopen(mnist_alternative_url)
        with open(mnist_save_path, "wb") as matlab_file:
            copyfileobj(mnist_url, matlab_file)

#Step 1. Downloading the Data (MNIST)

print(get_data_home())

fetch_mnist()
mnist = fetch_mldata('MNIST original')

# These are the images
# There are 70,000 images (28 by 28 images for a dimensionality of 784)
print("Number of images: ", mnist.data.shape)
# These are the labels
print("Labels: " ,mnist.target.shape)


#Step 2.  Splitting Data into Training and Test Sets (MNIST)
train_img, test_img, train_lbl, test_lbl = train_test_split(
        mnist.data, mnist.target, test_size=1/7.0, random_state=0) 

tr_top=[img[:392] for img in train_img]
tr_bot=[img[392:] for img in train_img]
test_top=[img[:392] for img in test_img]
test_bot=[img[392:] for img in test_img]

tr_X = []

for i in range(len(tr_top)): 
    tr_X.append(np.dstack((tr_top[i], tr_bot[i])))


#Step 3. Showing the Images and Labels (MNIST)
plt.figure(figsize=(20,4))
for index, (image, label) in enumerate(zip(train_img[0:5], train_lbl[0:5])):
    plt.subplot(1, 5, index + 1)
    plt.imshow(np.reshape(image, (28,28)), cmap=plt.cm.gray)
    plt.title('Training: %i\n' % label, fontsize = 20)
 

#Step 4. Now, it is time to choose the model, in this case it is a Logistic Regression model 
#(be sure you import the model.
#ie,from sklearn.linear_model import LogisticRegression)
# all parameters not specified are set to their defaults
# default solver is incredibly slow thats why we change it
#logisticRegr = LogisticRegression(solver = 'lbfgs')
    
improved = MLPClassifier(hidden_layer_sizes = 1, activation = "logistic", solver = "adam")


# Training the model on the data, storing the information 
#learned from the data.
#Model is learning the relationship between x (digits) and y (labels)

#logisticRegr.fit(train_img, train_lbl)

improved.fit(tr_X, train_lbl)


#Step 5. Predict the labels of new data (new images)
#Uses the information the model learned during the model training process
# Returns a NumPy Array
# Predict for One Observation (image)
#logisticRegr.predict(test_img[0].reshape(1,-1))

#Predict for Multiple Observations (images) at Once

#logisticRegr.predict(test_img[0:10])

#Predict the entire test data
#predictions = logisticRegr.predict(test_img)

predictions = improved.predict(test_X)

#Step 6. Measuring accuracy of the model
#score = logisticRegr.score(test_img, test_lbl)
score = improved.score(test_X, test_lbl)
print("Accuracy score: ",score)



#Step 7. Identifying Misclassified images and image labels
# and creating a confusion matrix 
index = 0
confusion_dict = {}
misclassifiedIndexes = []

for label, predict in zip(test_lbl, predictions):
    if label != predict: 
        misclassifiedIndexes.append(index)
        if not (label in confusion_dict.keys()):
            confusion_dict[label]=[predict]
        else:
            confusion_dict[label].append(predict)
    index +=1
 
all_labels = sorted(list(confusion_dict.keys()))
#label_cts = [len(confusion_dict[int(label)]) for label in all_labels]
label_cts = []
for label in all_labels:
    label_cts.append(len(confusion_dict[label]))
#confusion_mat = [[confusion_dict[int(label)].count(predict)/label_cts[int(label)] for predict in all_labels] for label in all_labels]
confusion_mat = []
for label in all_labels:
    predict_ratios = []
    for predict in all_labels:
        predict_ratios.append(confusion_dict[int(label)].count(predict)/label_cts[int(label)])
    confusion_mat.append(predict_ratios)

print("Confusion Matrix ",confusion_mat)
print(confusion_mat[8])

#######################################################################
#Confusion matrix using 'seaborn' python package
cm = metrics.confusion_matrix(test_lbl, predictions)
print(cm)
plt.figure(figsize=(9,9))
sns.heatmap(cm, annot=True, fmt=".3f", linewidths=.5, square = True, cmap = 'Blues_r');
plt.ylabel('Actual label');
plt.xlabel('Predicted label');
all_sample_title = 'Accuracy Score: {0}'.format(score)
plt.title(all_sample_title, size = 15);

#######################################################################

#Print the misclassified images
plt.figure(figsize=(20,4))
for plotIndex, badIndex in enumerate(misclassifiedIndexes[0:5]):
    plt.subplot(1, 5, plotIndex + 1)
    plt.imshow(np.reshape(test_img[badIndex], (28,28)), cmap=plt.cm.gray)
    plt.title('Predicted: {}, Actual: {}'.format(predictions[badIndex], test_lbl[badIndex]), fontsize = 15)

plt.show()

