from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
    def tearDown(self):
        self.browser.quit()
    def test_can_start_a_list_and_retrieve_it_later(self):
        #A peson goes to the website 'http://localhost:8000
        self.browser.get('http://localhost:8000')

        #They are treated with page with To-Do lists on the Title
        self.assertIn('To-Do lists',self.browser.title)

        #They find out that the heading of the page is also To-Do
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #They are then prompted with an input field where they have to put a tast that is needed to be done
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')

        #They Enter 'Buy peacock feathers' and then hit Enter.
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        #They then wait for the page to update 
        time.sleep(1)

        #They check whether their task is added in the list or not
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        self.assertIn('2: Use peacock feathers to make a fly', [row.text for row in rows])
        #PROGRAMMER DELIBERATELY FAILING THE TEST
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()