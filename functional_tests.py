'''Functional Tests'''
import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    """Test case for new visitor"""

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        """User story #1: Persistent To-Do List"""

        # Chi has once again heard about a cool new online to-do app. He goes
        # to check out its home page
        self.browser.get('http://localhost:8000')

        # He notices the page title and header mention to-do lists
        self.assertIn('To-do', self.browser.title)
        self.fail('Finish the test!')

        # He gets invited to enter a to-do item striaght away

        # He types "Reach 2k MMR" into a text box. (Chi's hobby is streaning
        # some dotes)

        # When he hits enter, the page updates, and now the page lists:
        # "1. Reach 2k MMR" as an item in a to-do list

        # There is still a text box inviting him to add another item. He
        # enters: "Stream some dotes" (Chi is a pro)

        # The page updates again, and now shows both items on his list

        # Chi expects the site to remember his list. Given his map awareness,
        # he sees the unique URL that the site generated for him and he assumes
        # that his expectation is met.

        # He visits that URL. His to do list shows up.

        # Satified, he closes his browser and goes back to the game.

        self.browser.quit()

# Check if this file is executed from the command line
if __name__ == '__main__':
    # Launches unittest test runner, which finds all test classes and methods
    # in the file and runs them
    unittest.main()
