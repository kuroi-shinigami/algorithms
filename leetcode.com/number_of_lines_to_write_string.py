#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from string import ascii_lowercase


class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        _widths = {x: y for x, y in zip(ascii_lowercase, widths)}
        _res = 0
        _lines = 1
        for symbol in S:
            _res += _widths[symbol]
            if _res > 100:
                _res = _widths[symbol]
                _lines += 1

        return [_lines, _res]
