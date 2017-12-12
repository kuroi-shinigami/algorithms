#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        juxtaposition = {'{': '}', '(': ')', '[': ']'}
        stack = []
        for bracket in s:
            if bracket in ['{', '(', '[']:
                stack.append(bracket)
            if bracket in ['}', ')', ']']:
                try:
                    if juxtaposition[stack[-1]] == bracket:
                        stack.pop(-1)
                    else:
                        return False
                except IndexError:
                    return False
        if stack:
            return False
        return True
