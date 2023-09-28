# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest
from tools_setup import my_brand
from math import sqrt

from triangle import classifyTriangle

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

