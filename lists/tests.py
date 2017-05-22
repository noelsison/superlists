"""Unit tests for lists app

Run `python manage.py test` in the console and django will automatically find
these tests.py files and run all TestCase along with their test_* functions
"""
from django.test import TestCase

from lists.models import Item, List
from lists.views import HOME_TEMPLATE_PATH, LIST_TEMPLATE_PATH


class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        # Get a HttpResponse object from Djangp
        response = self.client.get('/')

        # Check if it's using the expected template
        self.assertTemplateUsed(response, HOME_TEMPLATE_PATH)


class NewListTest(TestCase):
    def test_can_save_a_POST_request(self):
        self.client.post('/lists/new', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST_request(self):
        response = self.client.post(
            '/lists/new', data={'item_text': 'A new list item'})
        self.assertRedirects(
            response, '/lists/best-list-the-world-has-ever-seen/')


class ListAndItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item_text = 'The first list item this world has ever seen'
        second_item_text = 'Second item to represent our two superstars'

        list_ = List()
        list_.save()

        first_item = Item()
        first_item.text = first_item_text
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.text = second_item_text
        second_item.list = list_
        second_item.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, first_item_text)
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.text, second_item_text)
        self.assertEqual(second_saved_item.list, list_)


class ListViewTest(TestCase):
    def test_displays_all_items(self):
        first_item_text = 'The first list item this world has ever seen'
        second_item_text = 'Second item to represent our two superstars'

        list_ = List.objects.create()
        Item.objects.create(text=first_item_text, list=list_)
        Item.objects.create(text=second_item_text, list=list_)

        response = self.client.get('/lists/best-list-the-world-has-ever-seen/')

        self.assertContains(response, first_item_text)
        self.assertContains(response, second_item_text)

    def test_uses_list_template(self):
        response = self.client.get('/lists/best-list-the-world-has-ever-seen/')
        self.assertTemplateUsed(response, LIST_TEMPLATE_PATH)
