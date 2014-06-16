# -*- coding: utf-8 -*-

print(__doc__)

import re
import warnings

import numpy as np
import pylab as pl
from sklearn import svm 
from sklearn import preprocessing

class SVM():
    def __init__(self):
        return

    def load_tsv_file(self, filepath):
        return self.load_delimited_file(filepath , delimiter="\t")

    def load_csv_file(self, filepath):
        return self.load_delimited_file(filepath , delimiter=",")

    def load_delimited_file(self, filepath, delimiter):
        return np.genfromtxt(filepath, delimiter=delimiter, dtype=None)

    def transform_data(self, data, labels): 
        le = preprocessing.LabelEncoder()
        le.fit(labels)
        return le.transform(data)

    def train(self, data, labels):
        clf = svm.SVC(kernel='rbf', C=1)
        clf.fit(data, labels)
        return clf
