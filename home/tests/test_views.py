import re
from django.test import TestCase
from django.urls import reverse


class TestViews(TestCase):

    def test_home_page_status_200(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home/home.html')
