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
        new_list = List.objects.first()
        self.assertRedirects(
            response, f'/lists/{new_list.id}/')


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
    def test_displays_all_items_for_that_list(self):
        first_item_text = 'The first list item this world has ever seen'
        second_item_text = 'Second item to represent our two superstars'
        third_item_text = '3k MMR forever'
        fourth_item_text = '4k the dream'

        list_first = List.objects.create()
        Item.objects.create(text=first_item_text, list=list_first)
        Item.objects.create(text=second_item_text, list=list_first)

        list_second = List.objects.create()
        Item.objects.create(text=third_item_text, list=list_second)
        Item.objects.create(text=fourth_item_text, list=list_second)

        response = self.client.get(f'/lists/{list_first.id}/')

        self.assertContains(response, first_item_text)
        self.assertContains(response, second_item_text)
        self.assertNotContains(response, third_item_text)
        self.assertNotContains(response, fourth_item_text)

    def test_uses_list_template(self):
        list_ = List.objects.create()
        response = self.client.get(f'/lists/{list_.id}/')
        self.assertTemplateUsed(response, LIST_TEMPLATE_PATH)


class NewItemTest(TestCase):

    def test_can_save_a_POST_request_on_an_existing_list(self):
        new_item_text = 'Here comes a new challenger!'

        other_list = List.objects.create()  # pylint: disable=unused-variable
        # other_list tests for List.objects.first() hacks
        latest_list = List.objects.create()

        self.client.post(
            f'/lists/{latest_list.id}/add_item',
            data={'item_text': new_item_text}
        )

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, new_item_text)
        self.assertEqual(new_item.list, latest_list)

    def test_redirects_to_list_view(self):
        new_item_text = 'Here comes a new challenger!'

        other_list = List.objects.create()  # pylint: disable=unused-variable
        # other_list tests for List.objects.first() hacks
        latest_list = List.objects.create()

        response = self.client.post(
            f'/lists/{latest_list.id}/add_item',
            data={'item_text': new_item_text}
        )

        self.assertRedirects(response, f'/lists/{latest_list.id}/')

    def test_passes_correct_list_to_template(self):
        other_list = List.objects.create()  # pylint: disable=unused-variable
        # other_list tests for List.objects.first() hacks
        latest_list = List.objects.create()

        response = self.client.get(f'/lists/{latest_list.id}/')
        self.assertEqual(response.context['list'], latest_list)
