import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import Parser


class TestMap(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_function(input):
        def test(self):
            exec(input) in globals(), locals()
        return test

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    testsmap = Parser.parse()
    for test in testsmap.iteritems():
        test_func = test(test.input)
        setattr(TestMap, 'test_{0}'.format(test.id), test_func)

    unittest.main()
