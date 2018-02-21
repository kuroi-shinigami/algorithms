#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from string import ascii_uppercase


class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        if not s:
            return res
        numbers = {}
        for i in range(len(ascii_uppercase)):
            numbers.update({ascii_uppercase[i]: i+1})
        for ix, i in enumerate(range(len(s)-1, -1, -1)):
            res += numbers[s[i]]*(26**ix)
        return res
