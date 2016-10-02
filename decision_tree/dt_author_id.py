#!/usr/bin/python

"""
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:
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

from sklearn import tree
from sklearn.metrics import accuracy_score
import numpy as np

print "Results for Decision Tree:"

#print "Train features shape:", features_train.shape
clf = tree.DecisionTreeClassifier(min_samples_split=40)

t0 = time()  #check training Timing
clf = clf.fit(features_train, labels_train)
print "Training time:", round(time()-t0, 3), "s"

t1 = time()  #check prediction Timing
pred = clf.predict(features_test)
print "Prediction time:", round(time()-t1, 3), "s"

accuracy = accuracy_score(pred, labels_test)
print "Prediction Accuracy: ",accuracy



#############AAADDD DIFFERENT ALGOOOO###########################


print "------------==================----------------\n"

print "Results for KNN:"

from sklearn import neighbors, datasets

clf_neigb = neighbors.KNeighborsClassifier(10)
t0 = time()  #check training Timing
clf_neigb.fit(features_train, labels_train)
print "Training time:", round(time()-t0, 3), "s"

t1 = time()  #check prediction Timing
pred_neigb = clf_neigb.predict(features_test)
print "Prediction time:", round(time()-t1, 3), "s"

accuracy = accuracy_score(pred_neigb, labels_test)
print "Prediction Accuracy: ",accuracy

print "------------==================----------------\n"


print "Results for Random Forest:"

from sklearn.ensemble import RandomForestClassifier

clf_randforest = RandomForestClassifier(n_estimators=10)
t0 = time()  #check training Timing
clf_randforest = clf_randforest.fit(features_train, labels_train)
print "Training time:", round(time()-t0, 3), "s"

t1 = time()  #check prediction Timing
pred_randforest = clf_randforest.predict(features_test)
print "Prediction time:", round(time()-t1, 3), "s"

accuracy_randforest = accuracy_score(pred_randforest, labels_test)
print "Prediction Accuracy: ",accuracy_randforest

print "------------==================----------------\n"

print "Results for Adaboost:"

from sklearn.ensemble import AdaBoostClassifier

clf_adaboost = AdaBoostClassifier(n_estimators=100)

t0 = time()  #check training Timing
clf_adaboost = clf_adaboost.fit(features_train, labels_train)
print "Training time:", round(time()-t0, 3), "s"

t1 = time()  #check prediction Timing
pred_adaboost = clf_adaboost.predict(features_test)
print "Prediction time:", round(time()-t1, 3), "s"

accuracy_adaboost = accuracy_score(pred_adaboost, labels_test)
print "Prediction Accuracy: ",accuracy_adaboost

#########################################################
