#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """

        # import sys
        # int.from_bytes(bytes('1'*len(bin(num).split('b')[-1]), encoding='utf-8'), byteorder=sys.byteorder)

        return num ^ sum([2**i for i in range(len(bin(num).split('b')[-1]))])
