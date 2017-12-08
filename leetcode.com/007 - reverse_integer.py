#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # dishonest Python solution
        if x > 2**31:
            return 0
        minus = False
        if x < 0:
            x = abs(x)
            minus = True
        s = list(str(x))
        s.reverse()
        s = int(''.join(s))
        if s > 2**31:
            return 0
        return -s if minus else s
