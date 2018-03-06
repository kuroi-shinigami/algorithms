#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        for i in range(int(n/2)):
            if s[i] != s[n-i-1]:
                return self.recheck(s, i)
        return True

    def recheck(self, s, i):
        _n = len(s)
        s1 = s[:i] + s[i+1:]
        s2 = s[:_n-i-1] + s[_n-i:]
        # print(s1)
        # print(s2)
        for _s in s1, s2:
            n = len(_s)
            for i in range(int(n/2)):
                if _s[i] != _s[n-i-1]:
                    break
            else:
                return True
        return False
