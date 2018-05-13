from unittest import TestCase

from positions_of_large_groups import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.largeGroupPositions("abbxxxxzzy"), [[3, 6]])

    def test_1(self):
        self.assertEqual(s.largeGroupPositions("abc"), [])

    def test_2(self):
        self.assertEqual(s.largeGroupPositions("abcdddeeeeaabbbcd"), [[3, 5], [6, 9], [12, 14]])

    def test_3(self):
        self.assertEqual(s.largeGroupPositions("aaa"), [[0, 2]])
