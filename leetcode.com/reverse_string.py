#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        _s = ''
        for i in range(len(s)-1, -1, -1):
            _s += s[i]
        return _s
