#!/usr/bin/env python3

from rearrange import rearrange_name
import unittest


class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)

    """
    Edge cases are inputs to our code that produce unexpected results, 
    and are found at the extreme ends of the ranges of input we imagine 
    our programs will typically work with. Edge cases usually need special 
    handling in scripts in order for the code to continue to behave correctly.
    
    We have corrected the module rearrange.py to catch the error.
    """

    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)

    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_one_name(self):
        testcase = "Voltaire"
        expected = "Voltaire"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_no_comma(self):
        testcase = "Lovelace Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)


unittest.main()
