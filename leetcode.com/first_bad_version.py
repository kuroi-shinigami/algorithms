#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # WHAT THE HELL IS GOING ON?
        # WHY DO WE SUPPOSE THAT WE HAVE EXACTLY ONE "Bad version"?
        # for i in range(1, n+1):
        #     if isBadVersion(i):
        #         return i
        _min = 1
        _max = n
        while _min < _max:
            cmp = _min + (_max - _min) // 2
            if isBadVersion(cmp):
                _max = cmp
            else:
                _min = cmp + 1
        return _min
