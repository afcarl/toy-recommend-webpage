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

    def test_get_history_with_pickled_array(self):
        access_history = AccessHistory(key="hoge", history_pickle=pickle.dumps(["page-a", "page-b", "page-c", "page-a"]))
        access_history.save()
        result = AccessHistory.objects.get(key="hoge").get_history()
        self.assertEqual(result, ['page-a', 'page-b', 'page-c', 'page-a'])

    def test_summarize_history(self):
        access_history = AccessHistory(key="hoge", history_pickle=pickle.dumps(["page-a", "page-b", "page-c", "page-a"]))
        result = access_history.summarize_history()
        self.assertEqual(result, [2, 1, 1])
