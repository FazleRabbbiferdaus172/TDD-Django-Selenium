from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 10


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        # print('success')
        self.browser.quit()
        # pass

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_for_one_user(self):
        # You have heard about a new online to-do app. You go to
        # check out it's homepage
        self.browser.get(self.live_server_url)

        # You notice the page title and the header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # You are invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute(
            'placeholder'), 'Enter a to-do item')
        # You type "Buy peacock feather" into a text box
        inputbox.send_keys('Buy peacock feather')
        # when you hit enter, the page updates, and now the page lists
        # "1: Buy peacock feather" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feather')
        # There is still a text box inviting yo to add another item. You
        # enter "Use peacock feather to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feather to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on your list.
        self.wait_for_row_in_list_table('1: Buy peacock feather')
        self.wait_for_row_in_list_table(
            '2: Use peacock feather to make a fly')
        # You wonder weather the site will remember you list. Then you see
        # that the site has generated a unique URL for you -- there is some
        # explanatory text to that effect.

        # You visit that URL - your to-do list is still there.

        # Satisfied, you go back to sleep

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # You start a new to-do list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # You notice that your list has a unique URL
        your_list_url = self.browser.current_url
        self.assertRegex(your_list_url, '/lists/.+')

        # now a new user, Francis, comes along to the site

        # We use a new browser session to make sure that no information
        # of your's in coming through from cookies ets
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis visitis the homepage. There is no sign of your
        # list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Francis starts a new list by enterning a new item. He
        # is less interesting than you...
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Francis gets his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, your_list_url)

        # Again, there is no trace of your list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy milk', page_text)

        # satisfied, they both go to sleep
