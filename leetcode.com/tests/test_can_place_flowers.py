from unittest import TestCase

from can_place_flowers import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.canPlaceFlowers([1, 0, 0, 0, 1], 1), True)

    def test_1(self):
        self.assertEqual(s.canPlaceFlowers([1, 0, 0, 0, 1], 2), False)

    def test_2(self):
        self.assertEqual(s.canPlaceFlowers([0, 0, 1, 0, 0, 0, 1, 0, 0], 3), True)

    def test_3(self):
        self.assertEqual(s.canPlaceFlowers([1, 0, 0, 0, 0, 0, 1], 2), True)

    def test_4(self):
        self.assertEqual(s.canPlaceFlowers([0], 1), True)

    def test_5(self):
        self.assertEqual(s.canPlaceFlowers([0, 0, 1, 0, 0], 1), True)

    def test_6(self):
        self.assertEqual(s.canPlaceFlowers([0, 0], 2), False)

    def test_7(self):
        self.assertEqual(s.canPlaceFlowers([0, 0, 0], 2), True)

    def test_8(self):
        self.assertEqual(s.canPlaceFlowers([0, 0, 0, 0], 3), False)
