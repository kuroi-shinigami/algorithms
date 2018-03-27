from unittest import TestCase

from number_of_lines_to_write_string import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.numberOfLines(
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            "abcdefghijklmnopqrstuvwxyz"), [3, 60])

    def test_1(self):
        self.assertEqual(s.numberOfLines(
            [4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            "bbbcccdddaaa"), [2, 4])
