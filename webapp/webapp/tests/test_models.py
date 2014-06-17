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

    def test_get_history_with_incollect_value(self):
        access_history = AccessHistory(key="hoge", history_pickle="hoge")
        access_history.save()
        result = AccessHistory.objects.get(key="hoge").get_history()
        self.assertEqual(result, [])

    def test_update_history(self):
        access_history = AccessHistory(key="hoge", history_pickle=["page-b"])
        access_history.save()
        result = AccessHistory.objects.get(key="hoge")
        self.assertEqual(result.get_history(), ["page-b"])
        access_history.update_history("page-a")
        result = AccessHistory.objects.get(key="hoge")
        self.assertEqual(result.get_history(), ["page-b", "page-a"])

    def test_update_history(self):
        key = "fuga"
        history_pickle = [
                "page-a", "page-a", "page-a", "page-a", "page-a",
                "page-b", "page-b", "page-b", "page-b", "page-b",
                ]
        access_history = AccessHistory(key=key, history_pickle=history_pickle)
        access_history.save()
        result = AccessHistory.objects.get(key="fuga")
        self.assertEqual(result.get_history(), history_pickle)
        access_history.update_history("page-c")
        expected = [
                "page-a", "page-a", "page-a", "page-a", "page-b",
                "page-b", "page-b", "page-b", "page-b", "page-c",
                ]
        result = AccessHistory.objects.get(key="fuga")
        self.assertEqual(result.get_history(), expected)


    def test_summarize_history(self):
        access_history = AccessHistory(key="hoge", history_pickle=pickle.dumps(["page-a", "page-b", "page-c", "page-a"]))
        result = access_history.summarize_history()
        self.assertEqual(result, [2, 1, 1])
