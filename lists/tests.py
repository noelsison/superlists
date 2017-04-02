"""Unit tests for lists app

Run `python manage.py test` in the console and django will automatically find
these tests.py files and run all TestCase along with their test_* functions
"""
from django.test import TestCase

from lists.models import Item
from lists.views import HOME_TEMPLATE_PATH


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


class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item_text = 'The first list item this world has ever seen'
        second_item_text = 'Second item to represent our two superstars'

        first_item = Item()
        first_item.text = first_item_text
        first_item.save()

        second_item = Item()
        second_item.text = second_item_text
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, first_item_text)
        self.assertEqual(second_saved_item.text, second_item_text)
