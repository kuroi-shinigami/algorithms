#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vovels = {"a", "e", "o", "i", "u"}
        vovels = vovels | {x.upper() for x in vovels}
        _t = []
        _r = []
        for x in s:
            if x not in vovels:
                _t.append(x)
            else:
                _t.append(None)
                _r.append(x)
        for i in range(len(_t)):
            if not _t[i]:
                _t[i] = _r.pop(-1)
        return "".join(_t)
