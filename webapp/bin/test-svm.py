#!/usr/bin/env python3
#coding:utf-8

import os
import sys

PROJECT_HOME=os.path.dirname( os.path.abspath(__file__)) + "/../"
sys.path.append(PROJECT_HOME)

from model.svm import SVM

model = SVM()

## load test data
data_filepath   = os.path.dirname(__file__) + "/../../resources/data/test-data.tsv"
labels_filepath = os.path.dirname(__file__) + "/../../resources/data/test-label.tsv"
data   = model.load_tsv_file(data_filepath)
labels = model.load_tsv_file(labels_filepath)

## restore model from file
result = model.predict_with_default_dumped_model(data)

num_true  = 0
num_false = 0
for i in range(0, len(labels)):
    if labels[i] == result[i]:
        num_true += 1
    else:
        num_false += 1

print("# trues : %d" % (num_true))
print("# falses: %d" % (num_false))
print("accurary: %f" % (num_true / (num_true + num_false)))
