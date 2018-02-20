from unittest import TestCase

from one_bit_and_two_bit_characters import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.isOneBitCharacter([1, 0, 0]), True)

    def test_1(self):
        self.assertEqual(s.isOneBitCharacter([1, 1, 1, 0]), False)

    def test_2(self):
        self.assertEqual(s.isOneBitCharacter([0, 0]), True)

    def test_3(self):
        self.assertEqual(s.isOneBitCharacter([0]), True)

    def test_4(self):
        self.assertEqual(s.isOneBitCharacter([1, 0]), False)

    def test_5(self):
        self.assertEqual(s.isOneBitCharacter([0, 1, 0]), False)

    def test_6(self):
        self.assertEqual(s.isOneBitCharacter(
            [1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0,
             1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1,
             0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1,
             1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1,
             0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0]), True)
