#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if needle in haystack:
            return len(haystack.split(needle)[0])
        else:
            return -1
