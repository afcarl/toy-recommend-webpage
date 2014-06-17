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

    def test_page_a(self):
        request = self.factory.get("/page-a/", HTTP_USER_AGENT='Mozilla/5.0')
        response = page_a(request)
        self.assertEqual(response.status_code, 200)

    def test_page_b(self):
        request = self.factory.get("/page-b/", HTTP_USER_AGENT='Mozilla/5.0')
        response = page_a(request)
        self.assertEqual(response.status_code, 200)

    def test_page_c(self):
        request = self.factory.get("/page-c/", HTTP_USER_AGENT='Mozilla/5.0')
        response = page_a(request)
        self.assertEqual(response.status_code, 200)
        
    def test_generate_user_id_hash(self):
        request = self.factory.get("/", HTTP_USER_AGENT='Mozilla/5.0')
        result = generate_user_id_hash(request)
        self.assertEqual(result, '6328c09c3f9c4817b14fddbb73d9602e1c09562e')

    def test_get_basic_parameters(self):
        request = self.factory.get("/page-a/", HTTP_USER_AGENT='Mozilla/5.0')
        result = get_basic_parameters(request)
        self.assertEqual(result, {'user_agent': 'Mozilla/5.0', 'client_ip_address': '127.0.0.1'})

    def test_get_client_ip(self):
        request = self.factory.get("/", HTTP_USER_AGENT = 'Mozilla/5.0')
        result  = get_client_ip(request)
        self.assertEqual(result, '127.0.0.1')

    def test_get_user_agent(self):
        request = self.factory.get("/", HTTP_USER_AGENT = 'Mozilla/5.0')
        result = get_user_agent(request)
        self.assertEqual(result, 'Mozilla/5.0')
