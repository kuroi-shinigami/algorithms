#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # leetcode says that THIS is faster than
        # return bin(int(a, 2)+int(b, 2))[2:]
        # __           __
        #   \__(X_X)__/
        #

        short, long = (a, b) if len(a) < len(b) else (b, a)
        short = short[::-1]
        long = long[::-1]
        _s = ""
        _transfer = 0
        for x, y in zip(short, long):
            _sum = int(x) + int(y) + int(_transfer)
            if _sum >= 2:
                _transfer = 1
            else:
                _transfer = 0
            _s += str(_sum % 2)
        _s = _s[::-1]
        # if _transfer:  # if not transfer - just copy
        for i in range(len(short), len(long)):
            _sum = int(long[i]) + int(_transfer)
            if _sum >= 2:
                _transfer = 1
            else:
                _transfer = 0
            _s = str(_sum % 2) + _s
        if _transfer:
            _s = str(_transfer) + _s
        return _s
