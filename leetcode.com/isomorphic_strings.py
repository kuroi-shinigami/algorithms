#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        _d1 = {}
        _d2 = {}
        for i in range(len(s)):
            _s = s[i]
            if _s in _d1:
                _d1[_s].append(i)
            else:
                _d1[_s] = [i]
            _t = t[i]
            if _t in _d2:
                _d2[_t].append(i)
            else:
                _d2[_t] = [i]
        return list(sorted(_d2.values())) == list(sorted(_d1.values()))
