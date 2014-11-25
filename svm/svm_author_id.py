#!/usr/bin/python

"""
    this is the code to accompany the Lesson 2 (SVM) mini-project

    use an SVM to identify emails from the Enron corpus by their authors

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

#########################################################

from sklearn.svm import SVC

# Linear kernel
#clf = SVC(kernel='linear')

# Rbf kernel and various C parameters
clf = SVC(kernel='rbf', C=10000.0)

# A Smaller Training Set
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t0 = time()
pred = clf.predict(features_test)
print "test time:", round(time()-t0, 3), "s"

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(labels_test, pred)
print "accuracy: ", accuracy

# Predict for element 10 of the test set? The 26th? The 50th?
# Data point numbers given here (10, 26, 50) assume a zero-indexed list.
print "10th element: ", pred[10], \
      "\n26th element: ", pred[26], \
      "\n50th element: ", pred[50]

# The number of predictions equal to class 1 == 'Chris'
print """The number  predicted to be in the "Chris": """, sum(pred == 1)
