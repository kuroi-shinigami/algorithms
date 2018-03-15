#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'

        result = self.countAndSay(n-1)
        counter = 0
        buf = ''
        _s = ''
        for x in result:
            if not buf:
                buf = x
            if x == buf:
                counter += 1
            else:
                _s += str(counter) + buf
                buf = x
                counter = 1
        if counter:
            _s += str(counter) + x
        return _s
