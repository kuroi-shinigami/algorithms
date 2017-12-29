#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # sum(int(octet) << ((3 - i) << 3) for i, octet in enumerate(some_str.split('.')))
        n = x ^ y
        count = 0
        while n > 0:
            count = count + 1
            n = n & (n - 1)
        return count
