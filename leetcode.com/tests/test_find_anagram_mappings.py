from unittest import TestCase

from find_anagram_mappings import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.anagramMappings([12, 28, 46, 32, 50], [50, 12, 32, 46, 28]), [1, 4, 3, 2, 0])
