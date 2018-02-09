#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if not num:
            return False
        for x in [2, 3, 5]:
            while not num % x:
                num = num // x
        return num == 1
