#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = str(num)
        while len(num) > 1:
            res = 0
            for x in num:
                res += int(x)
            num = str(res)
        return int(num)
