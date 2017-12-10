#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # ToDo: use multiply with index value of char?
        acc = 0
        s = list(s)
        max_i = len(s)-1
        _romans = {'I': 1,
                   'V': 5,
                   'X': 10,
                   'L': 50,
                   'C': 100,
                   'D': 500,
                   'M': 1000}
        for i, x in enumerate(s):
            if i < max_i:
                if _romans[s[i+1]] <= _romans[s[i]]:  # LX
                    acc += _romans[x]
                else:                          # IV
                    acc -= _romans[x]
            else:
                acc += _romans[x]
        return acc
