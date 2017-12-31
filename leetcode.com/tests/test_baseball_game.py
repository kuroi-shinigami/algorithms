from unittest import TestCase

from baseball_game import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.calPoints(["5", "2", "C", "D", "+"]), 30)

    def test_1(self):
        self.assertEqual(s.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]), 27)

    # noinspection PyBroadException
    def test_2(self):
        try:
            s.calPoints(["61", "-50", "65", "+", "D", "-99", "-58", "88", "19", "-11"])
        except Exception:
            self.fail()
