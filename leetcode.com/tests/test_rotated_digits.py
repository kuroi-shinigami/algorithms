#!/usr/bin/env python

from unittest import TestCase

from rotated_digits import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.rotatedDigits(10), 4)

    def test_1(self):
        self.assertEqual(s.rotatedDigits(2), 1)

    def test_2(self):
        self.assertEqual(s.rotatedDigits(5), 2)
