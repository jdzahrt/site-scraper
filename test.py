import unittest
from main import *


class TestIt(unittest.TestCase):
    def test_it(self):
        print("Hello")
        actual = get_user_info()
        expect = 'test123'
        self.assertEqual(actual, expect)
