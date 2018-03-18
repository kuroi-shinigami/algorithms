#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        _min = 1
        _max = n
        while _min != _max:
            cmp = _min + (_max - _min) // 2
            r = guess(cmp)
            if r == 0:
                return cmp
            elif r == -1:
                _max = cmp - 1
            else:
                _min = cmp + 1
        return _max
