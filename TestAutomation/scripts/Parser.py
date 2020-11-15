from glob import glob
import json
import os


def parse():
    testList = []

    for path in glob('./testCases/*.json'):  # loop over .json files in the cwd
        with open(path) as f:
            data = json.load(f)  # opent the json file
            test = testCase(data['id'], data['requirement'], data['component'], data['input'], data['output'])
            testList.append(test)
    return testList

class testCase:

    def __init__(self, id, req, component, input, output):
        self.id = id
        self.req = req
        self.component = component
        self.input = input
        self.output = output
