#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # for i in range(1, len(s)//2+1):
        #     # print(i, s[:i])
        #     # print(set(s.split(s[:i])))
        #     if len(set(s.split(s[:i]))) == 1:
        #         return True
        # return False

        return (s + s)[1:-1].find(s) != -1
