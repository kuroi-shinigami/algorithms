from unittest import TestCase

from subdomain_visit_count import Solution

s = Solution()


class TestSolution(TestCase):
    """"""

    def test_0(self):
        _answer = ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
        _res = s.subdomainVisits(["9001 discuss.leetcode.com"])
        self.assertEqual(set(_answer), set(_res))

    def test_1(self):
        _answer = s.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])
        _res = ["901 mail.com", "50 yahoo.com", "900 google.mail.com", "5 wiki.org", "5 org", "1 intel.mail.com",
                "951 com"]
        self.assertEqual(set(_answer), set(_res))
