from unittest import TestCase

from string_compression import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.compress(["a", "a", "b", "b", "c", "c", "c"]), 6)

    def test_1(self):
        self.assertEqual(s.compress(["a"]), 1)

    def test_2(self):
        self.assertEqual(s.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]), 4)

    def test_3(self):
        self.assertEqual(s.compress(["a", "a", "a", "b", "b", "a", "a"]), 6)
