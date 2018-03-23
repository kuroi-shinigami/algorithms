#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # if not x:
        #     return 0
        # for i in range(x):
        #     if i * i == x:
        #         return i
        #     if i*i > x:
        #         return i-1

        _min = 1
        _max = x
        while _min < _max:
            cmp = _min + (_max - _min) // 2
            _m = cmp*cmp
            if _m == x:
                return cmp
            elif _m > x:
                _max = cmp - 1
            else:
                _min = cmp + 1
        if _min*_min > x:
            return _min - 1
        else:
            return _min
