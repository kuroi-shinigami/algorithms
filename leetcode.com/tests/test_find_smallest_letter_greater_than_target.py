#!/usr/bin/env python

from unittest import TestCase

from find_smallest_letter_greater_than_target import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.nextGreatestLetter(["c", "f", "j"], "a"), "c")

    def test_1(self):
        self.assertEqual(s.nextGreatestLetter(["c", "f", "j"], "c"), "f")

    def test_2(self):
        self.assertEqual(s.nextGreatestLetter(["c", "f", "j"], "d"), "f")

    def test_3(self):
        self.assertEqual(s.nextGreatestLetter(["c", "f", "j"], "g"), "j")

    def test_4(self):
        self.assertEqual(s.nextGreatestLetter(["c", "f", "j"], "j"), "c")

    def test_5(self):
        self.assertEqual(s.nextGreatestLetter(["c", "f", "j"], "k"), "c")
