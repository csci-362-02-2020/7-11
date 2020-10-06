import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestMap(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
   
   #INSERT EACH TEST CASE HERE 

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
