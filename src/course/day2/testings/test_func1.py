import unittest

from .module1 import func1

class MyT(unittest.TestCase):


    def setUp(self):
        self.variable = 1



    def test_(self):
        self.assertEqual(1, func1(1))

    def test_func1_of_2(self):
        self.assertEquals(1, func1(1))

    def test_func1_of_7(self):
        self.assertEquals(6, func1(7))

    def test_func1_of_100(self):
        self.assertEquals(6, func1(100))
