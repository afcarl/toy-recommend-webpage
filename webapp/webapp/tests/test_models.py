# -*- coding: utf-8 -*- 
import os
import warnings
import pickle
from django.test import Client
from django.test import TestCase, RequestFactory
from webapp.models import AccessHistory

class TestAccessHistoryModel(TestCase):
    def test_save_without_pickled(self):
        access_history = AccessHistory(key="hoge", history_pickle="fuga")
        access_history.save()
        result = AccessHistory.objects.get(key="hoge")
        self.assertEqual(result.history_pickle, pickle.dumps("fuga"))

    def test_save_with_pickled(self):
        access_history = AccessHistory(key="hoge", history_pickle=pickle.dumps("fuga"))
        access_history.save()
        result = AccessHistory.objects.get(key="hoge")
        self.assertEqual(result.history_pickle, pickle.dumps("fuga"))

    def test_get_history_without_pickled(self):
        access_history = AccessHistory(key="hoge", history_pickle="fuga")
        access_history.save()
        result = AccessHistory.objects.get(key="hoge")
        self.assertEqual(result.history_pickle, pickle.dumps("fuga"))

    def test_get_history_with_pickled(self):
        access_history = AccessHistory(key="hoge", history_pickle=pickle.dumps("fuga"))
        access_history.save()
        result = AccessHistory.objects.get(key="hoge")
        self.assertEqual(result.history_pickle, pickle.dumps("fuga"))
