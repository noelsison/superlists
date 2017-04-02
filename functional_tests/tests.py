"""Functional Tests for superlists project

User Stories are placed within their respective test_* functions
Steps of the user story are enclosed in '''

"""
import time

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys

MAX_WAIT = 10


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        # Selenium browser object we'll use to access the resulting webpage
        self.browser = webdriver.Firefox()

    def check_for_row_in_list_table(self, expected_text):
        table = self.browser.find_element_by_id('id-list-table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(expected_text, [row.text for row in rows])

    def wait_for_row_in_list_table(self, expected_text):
        # TODO: Replace this with better code
        start_time = time.time()
        while True:
            try:
                self.check_for_row_in_list_table(expected_text)
                return
            except (AssertionError, WebDriverException) as error:
                # WebDriverException is when page hasn't loaded yet
                # AssertionError is when page isn't fully loaded yet
                if time.time() - start_time > MAX_WAIT:
                    raise error
                time.sleep(0.5)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        """ Test User Story #1: Persistent To-Do List """

        '''
        Chi has once again heard about a cool new online to-do app. He goes
        to check out its home page
        '''
        self.browser.get(self.live_server_url)

        '''
        He notices the page title and header mention to-do lists
        '''
        string_title = 'To-Do'
        self.assertIn(string_title, self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn(string_title, header_text)

        '''
        He gets invited to enter a to-do item striaght away
        '''
        string_instructions = 'Enter a to-do item'
        inputbox = self.browser.find_element_by_id('id-new-item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            string_instructions
        )

        '''
        He types "Reach 2k MMR" into a text box. (Chi's hobby is streaning
        some dotes)
        '''
        inputbox.send_keys('Reach 2k MMR')

        # When he hits enter, the page updates, and now the page lists:
        # "1. Reach 2k MMR" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('1: Reach 2k MMR')

        # There is still a text box inviting him to add another item. He
        # enters: "Stream some dotes" (Chi is a pro)
        inputbox = self.browser.find_element_by_id('id-new-item')
        inputbox.send_keys('Stream some dotes')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on his list
        self.wait_for_row_in_list_table('1: Reach 2k MMR')
        self.wait_for_row_in_list_table('2: Stream some dotes')

        # Chi expects the site to remember his list. Given his map awareness,
        # he sees the unique URL that the site generated for him and he assumes
        # that his expectation is met.
        self.fail('Finish the test!')
        # He visits that URL. His to do list shows up.

        # Satified, he closes his browser and goes back to the game.

        self.browser.quit()
