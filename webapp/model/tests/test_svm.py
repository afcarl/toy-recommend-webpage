# -*- coding: utf-8 -*-

import os
import nose
import warnings
import numpy as np
from nose.tools import *
from model.svm  import SVM
from sklearn    import preprocessing

def test_load_delimited_file():
    model = SVM()
    filepath = os.path.dirname(__file__) + "/data/test-data.tsv"
    data = model.load_delimited_file(filepath, "\t")
    expected = [
            (b'"C"', 1, 4, 0), (b'"C"', 0, 4, 1), (b'"C"', 0, 5, 1), 
            (b'"A"', 3, 2, 1), (b'"C"', 1, 7, 1), (b'"A"', 7, 3, 0), 
            (b'"C"', 0, 7, 0), (b'"C"', 0, 7, 0), (b'"B"', 0, 4, 5), 
            (b'"A"', 4, 0, 1)
        ]
    assert_equal(data.tolist(), expected)

def test_transform_data():
    model = SVM()
    data_filepath   = os.path.dirname(__file__) + "/data/test-data.tsv"
    labels_filepath = os.path.dirname(__file__) + "/data/test-data-label.tsv"
    warnings.warn(labels_filepath)
    data   = model.load_tsv_file(data_filepath)
    labels = model.load_tsv_file(labels_filepath)
    le = preprocessing.LabelEncoder()
    le.fit(labels)
    result = le.transform(data.tolist())
    assert_equal(result, [])
    #result = model.transform_data(data, labels)
    #assert_equal(labels, 1)
