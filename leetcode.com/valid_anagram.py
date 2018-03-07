#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # return not bool(set(s) ^ set(t))
        if len(s) != len(t):
            return False
        if set(s) ^ set(t):
            return False
        _s = {}
        _t = {}
        for x, y in zip(s, t):
            if x not in _s:
                _s[x] = 1
            else:
                _s[x] += 1
            if y not in _t:
                _t[y] = 1
            else:
                _t[y] += 1
        # print(_s)
        # print(_t)
        return _s == _t
