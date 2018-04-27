from unittest import TestCase

from shortest_distance_to_a_character import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_1(self):
        self.assertEqual(s.shortestToChar("loveleetcode", 'e'), [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0])

    def test_2(self):
        self.assertEqual(s.shortestToChar("aaba", 'b'), [2, 1, 0, 1])
