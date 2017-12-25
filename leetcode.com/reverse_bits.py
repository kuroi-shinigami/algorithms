#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        s = ''
        # print('00000010100101000001111010011100')
        # print('00111001011110000010100101000000')
        for x in reversed(bin(n).lstrip('-0b').zfill(32)):
            s += x

        # Somehow, didn't work
        # res = 0
        # s = ''
        # print('00000010100101000001111010011100')
        # print('00111001011110000010100101000000')
        # print(bin(n).lstrip('-0b').zfill(32))
        # for i, _s in enumerate(bin(n).lstrip('-0b').zfill(32)):
        #     res += (int(_s) * 2) ** i
        # res -= 1
        # return res

        return int('0b{}'.format(s), 2)


