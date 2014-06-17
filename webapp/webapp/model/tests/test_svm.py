# -*- coding: utf-8 -*- 
import os
import nose
import warnings
import numpy as np
from nose.tools import *
from webapp.model.svm  import SVM
from sklearn    import preprocessing
from sklearn    import svm


def test_load_delimited_file():
    model = SVM()
    filepath = os.path.dirname(__file__) + "/data/test-data.tsv"
    data = model.load_delimited_file(filepath, "\t")
    expected = [
            [3, 0, 9, 0], [3, 2, 8, 0], [1, 2, 3, 2],
            [3, 0, 9, 1], [2, 2, 1, 7], [2, 1, 1, 7],
            [2, 0, 3, 6], [2, 4, 1, 5], [2, 2, 1, 7],
            [2, 0, 2, 1]
            ]
    assert_equal(data.tolist(), expected)

def test_train():
    model = SVM()
    data_filepath   = os.path.dirname(__file__) + "/data/test-data.tsv"
    labels_filepath = os.path.dirname(__file__) + "/data/test-data-label.tsv"
    data   = model.load_tsv_file(data_filepath)
    labels = model.load_tsv_file(labels_filepath)
    clf = model.train(data, labels)

def test_dump_model():
    model = SVM()
    data_filepath   = os.path.dirname(__file__) + "/data/test-data.tsv"
    labels_filepath = os.path.dirname(__file__) + "/data/test-data-label.tsv"
    data   = model.load_tsv_file(data_filepath)
    labels = model.load_tsv_file(labels_filepath)
    clf = model.train(data, labels)
    pickled_filepath = os.path.dirname(__file__) + "/data/trained-svm.pickle"
    pickled_string = model.dump_model(pickled_filepath)
    assert(isinstance(pickled_filepath, str))
    assert_equal(len(pickled_string), 1809)

def test_loads_model_by_pickle():
    pickled_filepath = os.path.dirname(__file__) + "/data/trained-svm.pickle"
    model = SVM()
    clf = model.load_model_by_pickle(pickled_filepath)
    predict = clf.predict([3, 0, 9, 0])
    assert_equal(predict, [3])

def test_predict_with_dumped_model():
    model = SVM()
    target = [2, 0, 2, 1]
    filepath = os.path.dirname(__file__) + "/data/trained-svm.pickle"
    result = model.predict_with_dumped_model(target, filepath)
    assert_equal(result, [2])

def test_predict_with_default_dumped_model():
    model = SVM()
    target = [2, 0, 2, 1]
    result = model.predict_with_default_dumped_model(target)
    assert_equal(result, [2])
