#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the
### visualization code (prettyPicture) to show you the decision boundary


from sklearn.metrics import accuracy_score
from time import time

print "------------==================----------------\n"

print "Results for KNN:"

from sklearn import neighbors, datasets

clf_neigb = neighbors.KNeighborsClassifier(20,  algorithm='auto')
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

clf_randforest = RandomForestClassifier(n_estimators=20)
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

clf_adaboost = AdaBoostClassifier(n_estimators=20)

t0 = time()  #check training Timing
clf_adaboost = clf_adaboost.fit(features_train, labels_train)
print "Training time:", round(time()-t0, 3), "s"

t1 = time()  #check prediction Timing
pred_adaboost = clf_adaboost.predict(features_test)
print "Prediction time:", round(time()-t1, 3), "s"

accuracy_adaboost = accuracy_score(pred_adaboost, labels_test)
print "Prediction Accuracy: ",accuracy_adaboost


#try:
    #prettyPicture(clf, features_test, labels_test)
#except NameError:
#    pass
