from unittest import TestCase


from judge_route_circle import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        self.assertEqual(s.judgeCircle("UD"), True)

    def test_1(self):
        self.assertEqual(s.judgeCircle("LL"), False)

    def test_2(self):
        self.assertEqual(s.judgeCircle("XX"), False)
