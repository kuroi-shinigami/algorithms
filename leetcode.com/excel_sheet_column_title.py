#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from string import ascii_uppercase


class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ""
        while n:
            n -= 1
            res = ascii_uppercase[n % 26] + res
            n = n // 26
        return res
