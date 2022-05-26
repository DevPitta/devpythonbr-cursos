from django.test import TestCase
from django.urls import reverse


class TestViews(TestCase):

    def test_formations_page_status_200(self):
        response = self.client.get(reverse('formations'))
        self.assertEqual(response.status_code, 200)

    def test_formations_template(self):
        response = self.client.get(reverse('formations'))
        self.assertTemplateUsed(response, 'products/formations.html')

    def test_courses_page_status_200(self):
        response = self.client.get(reverse('courses'))
        self.assertEqual(response.status_code, 200)

    def test_courses_template(self):
        response = self.client.get(reverse('courses'))
        self.assertTemplateUsed(response, 'products/courses.html')
