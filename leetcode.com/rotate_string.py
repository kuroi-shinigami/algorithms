#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        if A in B+B:
            return True
        else:
            return False
