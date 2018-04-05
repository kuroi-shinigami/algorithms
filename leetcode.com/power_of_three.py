#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# from math import log


class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        # >>> log(243)/log(3)
        # 4.999999999999999
        # AHAHAHAH OH WOW
        # - - - - -
        # _res = log(n)/log(3)
        # return _res == int(_res)

        while n != 1:
            if n % 3 != 0:
                return False
            n = int(n/3)

        return True
