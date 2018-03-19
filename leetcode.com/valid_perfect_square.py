#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        _min = 1
        _max = num
        while _min < _max:
            cmp = _min + (_max - _min) // 2
            _m = cmp*cmp
            if _m == num:
                return True
            elif _m > num:
                _max = cmp - 1
            else:
                _min = cmp + 1
        return _min*_min == num

