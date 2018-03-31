from unittest import TestCase

from construct_the_rectangle import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.constructRectangle(4), [2, 2])

    def test_2(self):
        self.assertEqual(s.constructRectangle(3), [3, 1])

    def test_3(self):
        self.assertEqual(s.constructRectangle(15), [5, 3])

    def test_4(self):
        self.assertEqual(s.constructRectangle(18), [6, 3])
