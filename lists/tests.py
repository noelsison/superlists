"""Unit tests for lists app

Run `python manage.py test` in the console and django will automatically find
these tests.py files and run all TestCase along with their test_* functions
"""
from django.test import TestCase

from .views import HOME_TEMPLATE_PATH


class SmokeTest(TestCase):
    def test_home_page_returns_correct_html(self):
        # Get a HttpResponse object from Djangp
        response = self.client.get('/')

        # Check if it's using the expected template
        self.assertTemplateUsed(response, HOME_TEMPLATE_PATH)

    def test_can_save_a_POST_request(self):
        item_text_value = 'A new list item'
        response = self.client.post('/', data={'item_text': item_text_value})
        self.assertIn(item_text_value, response.content.decode())
        self.assertTemplateUsed(response, HOME_TEMPLATE_PATH)
