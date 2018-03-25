#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        _transfer = 1
        digits = digits[::-1]
        for i in range(len(digits)):
            _s = digits[i] + _transfer
            if _s >= 10:
                digits[i] = _s % 10
            else:
                digits[i] = _s
                # _transfer = 0
                break
        else:
            digits.append(1)
        return digits[::-1]
