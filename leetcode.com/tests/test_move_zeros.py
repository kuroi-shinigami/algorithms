from unittest import TestCase


from move_zeros import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.moveZeroes([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])

    def test_1(self):
        self.assertEqual(s.moveZeroes([0, 1, 0]), [1, 0, 0])

    def test_2(self):
        self.assertEqual(s.moveZeroes([0, 1]), [1, 0])

    def test_3(self):
        self.assertEqual(s.moveZeroes([0, 0, 1]), [1, 0, 0])
