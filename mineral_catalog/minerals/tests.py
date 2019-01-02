from datetime import datetime as dt

from django.test import TestCase
from django.test import Client

from .models import Mineral

# Create your tests here.
client = Client(HTTP_USER_AGENT='Mozilla/5.0')


class Test_MineralModel(TestCase):
    def test_A_blank_DB(self):
        '''This test function tests that the test database has loaded,
and has no minerals in it yet'''
        minerals = Mineral.objects.all()
        self.assertEqual(minerals.count(), 0)

    def test_B_load_DB(self):
        '''This test function tests loading the test database from json,
and now has mineral data loaded in it'''
        Mineral.load_from_json()
        minerals = Mineral.objects.all()
        self.assertEqual(minerals.count(), 874)

    def test_C_newMineral(self):
        '''This test function tests creating a new test mineral
'''
        mineral = Mineral(name='Kryptonite')
        mineral.save()
        self.assertLess(dt.now(), mineral.created_at.replace(tzinfo=None))
        self.assertEqual(mineral.name, 'Kryptonite')


class Test_Views(TestCase):
    def test_E_mineralList(self, client=client):
        r = client.get('/')
        self.assertIn(b"They're not rocks, but they totally rock!", r.content)
        self.assertIn(b"Aegirine", r.content)
        self.assertIn(b"Zoisite", r.content)

    def test_E_mineralDetail(self, client=client):
        Mineral.load_from_json()
        r = client.get('/146_detail/')
        self.assertIn(b"This mineral rocks!", r.content)
        self.assertIn(b"Bunsenite", r.content)

    def test_E_randomMineral(self, client=client):
        Mineral.load_from_json()
        r = client.get('/random/')
        self.assertTrue(r.__dict__['_headers']['location'])
