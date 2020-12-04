'''
PARSER.PY

This function parses all .json test case files in the testCases folder. The data for each file is stored as a testCase object. 
The parse function returns a list of testCase objects to the driver. 
'''

from glob import glob
import json
import os

# the parse function - loops over the .json test cases files, creating a list of test case objects
def parse():
    testList = []

    for path in glob('./testCases/*.json'):  # loop over .json files in the cwd
        with open(path) as f:
            data = json.load(f)  # open the .json file
            test = testCase(data['id'], data['requirement'], data['component'], data['input'], data['output'])
            testList.append(test)
    testList.sort(key=lambda x: x.id, reverse=False)
    return testList


# the test case class - each test case object created by the parser is an instance
class testCase:

    def __init__(self, id, req, component, input, output):
        self.id = id
        self.req = req
        self.component = component
        self.input = input
        self.output = output
