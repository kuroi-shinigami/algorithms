#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = bin(n)
        # print(s)
        for i in range(3, len(s)):
            # print(s[i-1], s[i])
            if s[i] == s[i-1]:
                return False
        return True