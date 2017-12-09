#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x = list(str(x))
        """
        >>> x = [1, 3, 1]
        >>> int(len(x)/2)
        1
        Actively using it. 
        If len = 2k + 1, we do not check 'central' element, if len = 2k, we will check only half of list
        """
        for i in range(int(len(x)/2)):
            if x[i] != x[-(i+1)]:
                return False
        return True
