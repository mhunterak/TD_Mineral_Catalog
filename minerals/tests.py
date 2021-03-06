from datetime import datetime as dt

from django.test import TestCase
from django.test import Client
from django.urls import reverse

from .models import Mineral

# Create your tests here.
client = Client(HTTP_USER_AGENT='Mozilla/5.0')


class Test_MineralModel(TestCase):
    def test_A_blank_DB(self):
        '''This test function tests that the test database has loaded,
and has the old minerals list in it yet'''
        minerals = Mineral.objects.all()
        self.assertEqual(minerals.count(), 874)

    def test_B_load_DB(self):
        '''This test function tests loading the test database from json,
and now has the new mineral data loaded in it'''
        Mineral.load_from_json()
        minerals = Mineral.objects.all()
        self.assertEqual(minerals.count(), 1748)

    def test_C_newMineral(self):
        '''This test function tests creating a new test mineral
'''
        mineral = Mineral(name='Kryptonite')
        mineral.save()
        self.assertLess(dt.now(), mineral.created_at.replace(tzinfo=None))
        self.assertEqual(mineral.name, 'Kryptonite')


class Test_Views(TestCase):
    def test_E_mineralList(self, client=client):
        r = client.get('/filter_letter/A')
        self.assertIn(b"They're not rocks, but they totally rock!", r.content)
        self.assertIn(b"Aegirine", r.content)
        self.assertIn(b"Azurite", r.content)

    def test_E_mineralDetail(self, client=client):
        Mineral.load_from_json()
        r = client.get('/detail/146')
        self.assertIn(b"This mineral rocks!", r.content)
        self.assertIn(b"Bunsenite", r.content)

    def test_E_randomMineral(self, client=client):
        Mineral.load_from_json()
        r = client.get('/random/')
        self.assertEqual(r.status_code, 302)
