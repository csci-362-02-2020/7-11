import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import Parser


class TestMap(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:3000")

    def test_function(input):
        def test(self):
            exec(input) in globals(), locals()
        return test

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":

    testsmap = Parser.parse()

    for test in testsmap:
        test_func = TestMap.test_function(test.input)
        setattr(TestMap, 'test_{0}'.format(test.id), test_func)

    # generate the HTML report
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../reports', report_name='testReport',open_in_browser=True))
