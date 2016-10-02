#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()



#########################################################
### your code goes here ###

from sklearn.svm import SVC

i=10000

clf = SVC(kernel="rbf", C=i)

t0 = time()
#features_train = features_train[:len(features_train)/100] #cut training data to 1%
#labels_train = labels_train[:len(labels_train)/100] #cut training data to 1%
clf.fit(features_train, labels_train)
print "Training time with C=",i," is:", round(time()-t0, 3), "s"

t1 = time()
pred = clf.predict(features_test)
print "Prediction with C=",i," is:", round(time()-t1, 3), "s"


from sklearn.metrics import accuracy_score
accuracy = accuracy_score(pred, labels_test)

print "Prediction Accuracy with C=",i," is:",accuracy

counter_1 = 0
for x in pred:
    if x == 1:          # if email from Chris
        counter_1 +=1

print counter_1

print "------------============-------------"


#########################################################
