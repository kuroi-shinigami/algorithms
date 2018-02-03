#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if not n % 4:
            return False
        else:
            return True
