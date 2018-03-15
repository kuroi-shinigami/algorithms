from unittest import TestCase


from count_and_say import Solution

s = Solution()


class TestSolution(TestCase):

    def test_0(self):
        self.assertEqual(s.countAndSay(1), '1')

    def test_1(self):
        self.assertEqual(s.countAndSay(2), '11')

    def test_2(self):
        self.assertEqual(s.countAndSay(3), '21')

    def test_3(self):
        self.assertEqual(s.countAndSay(4), '1211')

    def test_4(self):
        self.assertEqual(s.countAndSay(10), '13211311123113112211')

    def test_5(self):
        self.assertEqual(s.countAndSay(20), '11131221131211132221232112111312111213111213211231132132211211131221131211221321123113213221123113112221131112311332211211131221131211132211121312211231131112311211232221121321132132211331121321231231121113112221121321133112132112312321123113112221121113122113121113123112112322111213211322211312113211')

