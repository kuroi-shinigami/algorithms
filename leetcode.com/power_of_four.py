#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from math import log


class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        # while num != 1:
        #     if num % 4 != 0:
        #         return False
        #     num = int(num/4)
        #
        # return True
        _res = log(num)/log(4)
        return _res == int(_res)

