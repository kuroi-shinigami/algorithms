#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        def calc(some_str):
            _res = {}
            for x in some_str:
                if x not in _res:
                    _res[x] = 1
                else:
                    _res[x] += 1
            return _res

        m = calc(magazine)
        r = calc(ransomNote)
        for k in r:
            if k not in m:
                return False
            if m[k]<r[k]:
                return False
        return True
