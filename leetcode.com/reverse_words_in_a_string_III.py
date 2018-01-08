#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(["".join(reversed(x)) for x in s.split()])
