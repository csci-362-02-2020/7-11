'''
TESTMAP.PY

testmap.py is the main driver of the testing framework. It iterates over the list of testCase objects and executes the Python test code within each. It passes the results of the test to HTMLTestRunner.
'''

# import packages
import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import Parser

# TestMap class - uses the unittest testing framework
class TestMap(unittest.TestCase):
       
    # sets up the driver
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:3000")

    # executes the input from each test case
    def test_function(input):
        def test(self):
            exec(input) in globals(), locals()
        return test

    # tears down the driver
    def tearDown(self):
        self.driver.quit()

        
if __name__ == "__main__":

    # create an instance of the parser
    testsmap = Parser.parse()

    # loop through execution of the test cases using the test_function function
    for test in testsmap:
        test_func = TestMap.test_function(test.input)
        setattr(TestMap, 'test_{0}'.format(test.id), test_func)

    # create custom template arguments that allow us to pass testmap
    template_args = {
    "testCase_list": testsmap
    }

    # call HTML test runner to create and open an HTML report using our custom template
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(template='./scripts/template.html', template_args=template_args, output='../reports', report_name='testReport', open_in_browser=True, report_title='TestMap component test'))


