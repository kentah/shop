import unittest

from django.test import TestCase as dTestCase, Client
from django.core.urlresolvers import resolve
from .models import JoinForm


class PageRender(unittest.TestCase):

    def setUp(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get('/store/index/')
        self.assertEqual(response.status_code, 200)

    def test_shop(self):
        response = self.client.get('/store/shop/')
        self.assertEqual(response.status_code, 200)
    
    def test_join(self):
        response = self.client.get('/store/join/')
        self.assertEqual(response.status_code, 200)

    ''' the sign in test may need to render data in order to work
    def test_sign_in(self):
        response = self.client.get('/store/sign_in/')
        self.assertEqual(response.status_code, 200)
    '''
    
    def test_terms(self):
        response = self.client.get('/store/terms/')
        self.assertEqual(response.status_code, 200)

    def test_privacy(self):
        response = self.client.get('/store/privacy/')
        self.assertEqual(response.status_code, 200)

    def test_cart(self):
        response = self.client.get('/store/cart/')
        self.assertEqual(response.status_code, 200)
        

class JoinFormTestCase(dTestCase):

    ''' database testing of JoinForm for join.html '''

    def setUp(self):
        JoinForm.objects.create(first_name='Sparky', last_name='Fireside',
                                username='matches', password='peaches',
                                email='hydrophobic@cinder.com')


    def test_user_created(self):
        user = JoinForm.objects.get(first_name='Sparky')
        self.assertEqual(user.first_name, 'Sparky')
        self.assertEqual(user.last_name, 'Fireside')
        self.assertEqual(user.username, 'matches')
        self.assertEqual(user.password, 'peaches')
        self.assertEqual(user.email, 'hydrophobic@cinder.com')
       
    def test_user_updatable(self):
        user = JoinForm.objects.get(first_name='Sparky')
        user.first_name = 'Spanky'
        user.password = '&cream'
        self.assertEqual(user.first_name, 'Spanky')
        self.assertEqual(user.password, '&cream')

    def test_user_can_log_in(self):
        pass

