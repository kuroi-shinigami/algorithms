#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        _min = 0
        _max = int(c**0.5)
        while _min <= _max:
            _s = _min**2 + _max**2
            if _s == c:
                return True
            elif _s < c:
                _min += 1
            else:
                _max -= 1
        return False
