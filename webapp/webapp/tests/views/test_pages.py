# -*- coding: utf-8 -*- 
import os
import warnings
from django.test import Client
from django.test import TestCase, RequestFactory
from webapp.views.pages import *

class TestPagesView(TestCase):

    def setUp(self):
        self.client  = Client()
        self.factory = RequestFactory()

    #def test_product_index(self):
    #    response = self.client.get("/fruits/")
    #    nt.assert_equal(response.content, "The index")

    #def test_product_show(self):
    #    response = self.client.get("/fruits/papaya")
    #    nt.assert_equal(response.content, "Show the papaya page")

    #def test_product_add(self):
    #    response = self.client.get("/fruits/add")
    #    nt.assert_equal(response.content, "Add a fruit")

    def test_generate_user_id_hash(self):
        request = self.factory.get("/", HTTP_USER_AGENT='Mozilla/5.0')
        result = generate_user_id_hash(request)
        self.assertEqual(result, '6328c09c3f9c4817b14fddbb73d9602e1c09562e')
