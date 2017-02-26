'''Functional Tests'''

from selenium import webdriver

browser = webdriver.Firefox()  # pylint: disable=C0103
browser.get('http://localhost:8000')

assert "Django" in browser.title
