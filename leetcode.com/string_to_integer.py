#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        minus = False
        str = str.strip()
        if '+-' in str or '-+' in str or '--' in str:
            return 0
        if ' ' in str:
            if '+0' in str or '-0' in str:
                return 0
            if '+ ' in str or '- ' in str:
                return 0

        if str.startswith('-'):
            minus = True
            str = str[1:]
            if '+' in str:
                return 0
        while str:
            try:
                str = int(str)
                if str >= 2 ** 31:
                    if not minus:
                        str = 2 ** 31 - 1
                    else:
                        str = 2 ** 31
                break
            except (ValueError, TypeError):
                str = str[:len(str) - 1]
        if not str:
            return 0
        else:

            return -str if minus else str
