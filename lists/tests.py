"""Unit tests for lists app

Run `python manage.py test` in the console and django will automatically find
these tests.py files and run all TestCase along with their test_* functions
"""
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page


class SmokeTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        # Look for the object (function in this example) that handles '/' in
        # urls.py
        found = resolve('/')
        # Compare it with the function that we expect to use
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        # Make a HttpRequest object, which is What Django will see when a user
        # asks for a page
        request = HttpRequest()

        # Get a HttpResponse object from our view function
        response = home_page(request)

        # Extract raw bytes (.content) from the response and convert it to a
        # HTML string using .decode('utf8)
        html = response.content.decode('utf8')

        # Check if the html contains our required content
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))
