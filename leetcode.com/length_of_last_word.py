#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.split(" ")
        res = 0
        for i in range(len(s)-1, -1, -1):
            _res = len(s[i])
            if _res > 0:
                return _res
        return res
