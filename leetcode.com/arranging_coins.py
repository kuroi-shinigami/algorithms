#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        k = 1
        while n:
            n -= k
            if n < 0:
                return k - 1
            k += 1
        return k - 1
