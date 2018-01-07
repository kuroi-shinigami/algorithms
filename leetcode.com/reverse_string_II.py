#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = ''
        while s:
            # ToDo: use 2*k in one step?
            res += "".join(reversed(s[:k]))
            s = s[k:]
            res += s[:k]
            s = s[k:]
        return res
