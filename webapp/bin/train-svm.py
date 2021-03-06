#!/usr/bin/env python3
#coding:utf-8

import os
import sys

PROJECT_HOME=os.path.dirname( os.path.abspath(__file__)) + "/../"
sys.path.append(PROJECT_HOME)

from webapp.recommend.svm import SVM

## traininn
model = SVM()
data_filepath   = os.path.dirname(__file__) + "/../../resources/data/train-data.tsv"
labels_filepath = os.path.dirname(__file__) + "/../../resources/data/train-label.tsv"
data   = model.load_tsv_file(data_filepath)
labels = model.load_tsv_file(labels_filepath)
clf = model.train(data, labels)

## save default model
model.dump_default_model()
