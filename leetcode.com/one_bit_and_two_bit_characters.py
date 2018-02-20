#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        # while bits:
        #     if bits == [0]:
        #         return True
        #     if not bits[0]:
        #         bits = bits[1:]
        #     else:
        #         bits = bits[2:]
        #     print(bits)
        # return False
        res = []
        buf = []
        for x in bits:
            buf.append(x)
            if x == 0:
                res.append(buf)
                buf = []
            else:
                if len(buf) == 2:
                    res.append(buf)
                    buf = []
        return res[-1] == [0]


