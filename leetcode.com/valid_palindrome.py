#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from string import ascii_letters


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        _s = set(ascii_letters) | set(str(x) for x in range(10))
        r = ''
        for x in s:
            if x in _s:
                r += x.lower()
        n = len(r)
        print(r)
        for i in range(int(n/2)):
            if r[i] != r[n-i-1]:
                return False
        return True
