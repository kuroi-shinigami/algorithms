#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        _a = set(A)
        _b = set(B)
        # print(_a ^ _b)
        if B in A:
            return 1
        if _a ^ _b:
            return -1
        else:
            start = len(B)//len(A)
            while start <= len(B):
                if B in start*A:
                    return start
                start += 1
        return -1
