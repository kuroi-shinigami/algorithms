#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def clean(some_str):
    i = 0
    s = some_str
    n = len(s)
    while i < n:
        if n > 0:
            if s[i] == '#':
                idx = i-1 if i-1 >= 0 else 0
                left = s[:idx]
                if left == '#':
                    left = ''
                right = s[i + 1:]
                s = left + right
                # print(s)
                if i > 0:
                    i -= 1
            else:
                i += 1
        else:
            break
        n = len(s)
    return s


class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        if S == T:
            return True
        s = clean(S)
        # print(s)
        t = clean(T)
        # print(t)
        return s == t
