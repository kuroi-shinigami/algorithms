from unittest import TestCase

from add_binary import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_1(self):
        self.assertEqual(s.addBinary("11", "1"), "100")

    def test_2(self):
        self.assertEqual(s.addBinary("1010", "1011"), "10101")

    def test_3(self):
        self.assertEqual(s.addBinary("101111", "10"), "110001")
