#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n > 0:
            return bin(n).count('1') == 1
        else:
            return False
