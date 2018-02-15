#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        groups = []
        _len = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                _len += 1
            else:
                groups.append(_len)
                _len = 1
        groups.append(_len)
        # print(groups)
        for i in range(1, len(groups)):
            res += min(groups[i], groups[i-1])
        return res
