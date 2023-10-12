# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest
import requests
import mock
import json
from tools_setup import my_brand
from math import sqrt

from triangle import classifyTriangle

r = open('repos.json')

repos = json.load(r)
print(repos[0].get('name'))

c = open('commits.json')

commits = json.load(c)
print(len(commits))

class Fetch:
    def fetch_json(self, url):
        response = requests.get(url)
        return response.json()


def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == 'https://api.github.com/users/richkempinski/repos':
        return MockResponse(repos, 200)
    elif args[0] == 'https://api.github.com/repos/richkempinski/hellogitworld/commits':
        return MockResponse(commits, 200)

    return MockResponse(None, 404)

class TestReposAndCommits(unittest.TestCase):
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_fetch(self, mock_get):
        server = Fetch()
        repos = server.fetch_json('https://api.github.com/users/richkempinski/repos')
        self.assertEqual(repos[0].get('name'), 'csp')
        self.assertEqual(repos[1].get('name'), 'hellogitworld')
        call = 'https://api.github.com/repos/richkempinski/' + repos[1].get('name') + '/commits'
        print(call)
        commits = server.fetch_json(call)
        self.assertEqual(len(commits), 30)


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    def testSetEquil(self): # test invalid inputs
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral')
        self.assertNotEqual(classifyTriangle(15,34,32), 'Equilateral')
        self.assertNotEqual(classifyTriangle(5,5,4), 'Equilateral')
        self.assertNotEqual(classifyTriangle(3,4,5), 'Equilateral')

    # Right will take proirity over scalene
    def testSetScale(self):
        self.assertEqual(classifyTriangle(15,32,34), 'Scalene')
        self.assertNotEqual(classifyTriangle(1,1,1), 'Scalene')
        self.assertNotEqual(classifyTriangle(3,4,5), 'Scalene')

    # Isosceles will take proirity over right triangle
    def testSetRight(self):
        self.assertEqual(classifyTriangle(3,4,5), 'Right')
        self.assertNotEqual(classifyTriangle(1,1,sqrt(2)), 'Right')

if __name__ == '__main__':
    my_brand("HW 01: Testing Triangle Classification")
    unittest.main()

