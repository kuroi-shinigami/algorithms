from unittest import TestCase


from simplify_path import Solution

s = Solution()


class TestSolution(TestCase):

    def test_0(self):
        self.assertEqual(s.simplifyPath('/home/'), '/home')

    def test_1(self):
        self.assertEqual(s.simplifyPath('/a/./b/../../c/'), '/c')

    def test_2(self):
        self.assertEqual(s.simplifyPath('/'), '/')

    def test_3(self):
        self.assertEqual(s.simplifyPath('/../'), '/')

    def test_4(self):
        self.assertEqual(s.simplifyPath('/../abcde/../../../../1488/abcde'), '/1488/abcde')

    def test_5(self):
        self.assertEqual(s.simplifyPath('/home//foo/'), '/home/foo')
