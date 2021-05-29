from selenium import webdriver
import unittest


class NewUnitTest(unittest.TestCase):
    def setup(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # You have heard about a new online to-do app. You go to
        # check out it's homepage
        self.browser.get('http://localhost:8000')

        # You notice the page title and the header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test')

        # You are invited to enter a to-do item straight away

        # You type "Buy pet snake" into a text box

        # when you hit enter, the page updates, and now the page lists
        # "1: Buy pet snake" as an item in a to-do list

        # There is still a text box inviting yo to add another item. You
        # enter "Pet the snake"

        # The page updates again, and now shows both items on your list.

        # You wonder weather the site will remember you list. Then you see
        # that the site has generated a unique URL for you -- there is some
        # explanatory text to that effect.

        # You visit that URL - your to-do list is still there.

        # Satisfied, you go back to sleep


if __name__ == '__main__':
    unittest.main(warnings='ignore')
