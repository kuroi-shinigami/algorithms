from unittest import TestCase


from contains_duplicate import Solution

s = Solution()


class TestSolution(TestCase):

    def test_0(self):
        self.assertEqual(s.containsDuplicate([]), False)

    def test_1(self):
        self.assertEqual(s.containsDuplicate([0]), False)
