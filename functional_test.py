from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        # print('success')
        self.browser.quit()
        # pass

    def test_can_start_a_list_and_retrieve_it_later(self):
        # You have heard about a new online to-do app. You go to
        # check out it's homepage
        self.browser.get('http://localhost:8000')

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
        time.sleep(1)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        # print(rows)

        self.assertTrue(any(row.text == '1: Buy peacock feather'
                            for row in rows))
        # There is still a text box inviting yo to add another item. You
        # enter "Pet the snake"
        self.fail('Finish the test!')
        # The page updates again, and now shows both items on your list.

        # You wonder weather the site will remember you list. Then you see
        # that the site has generated a unique URL for you -- there is some
        # explanatory text to that effect.

        # You visit that URL - your to-do list is still there.

        # Satisfied, you go back to sleep


if __name__ == '__main__':
    unittest.main(warnings='ignore')
