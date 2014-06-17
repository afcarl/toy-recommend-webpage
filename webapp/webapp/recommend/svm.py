# -*- coding: utf-8 -*-

print(__doc__)

import re
import warnings
import os

import numpy as np
import pylab as pl
import pickle
import codecs
from sklearn import svm 
from sklearn import preprocessing

class SVM():
    def __init__(self):
        self.clf = svm.SVC(kernel='rbf', C=1)
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
        self.clf.fit(data, labels)
        return self.clf

    def dump_model(self, outfile):
        pickled_string = pickle.dumps(self.clf)
        file = open(outfile, 'wb')
        file.write(pickled_string)
        file.close
        return pickled_string

    def dump_default_model(self):
        filepath = self.get_default_dumped_model_path()
        self.dump_model(filepath)

    def load_model_by_pickle(self, filepath):
        file = open(filepath, "rb")
        self.clf = pickle.load(file)
        file.close
        return self.clf

    def predict_with_dumped_model(self, target, filepath):
        clf = self.load_model_by_pickle(filepath)
        return clf.predict(target)

    def predict_with_default_dumped_model(self, target):
        filepath = self.get_default_dumped_model_path()
        return self.predict_with_dumped_model(target, filepath)

    def get_default_dumped_model_path(self):
        return os.path.dirname(__file__) + "/../../resources/trained-svm.pickle"
