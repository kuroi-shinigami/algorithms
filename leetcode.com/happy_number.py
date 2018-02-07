#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        res = n
        cycle = set()
        while res not in cycle:
            cycle.add(res)
            res = 0
            for x in str(n):
                res += int(x)**2
            # print(res)
            if res == 1:
                return True
            n = res
        return False
