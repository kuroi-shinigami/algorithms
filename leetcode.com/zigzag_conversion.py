#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        if numRows == 2:
            return s[::2] + s[1::2]
        rows = [[] for x in range(numRows)]
        while s:
            try:
                for i, x in enumerate(rows):
                    x.append(s[i])
                s = s[i+1:]
            except IndexError:
                break
            try:
                for i, x in enumerate(rows[1:-1][::-1]):
                    x.append(s[i])
                s = s[i+1:]
            except IndexError:
                break

            print("- "*5)
            for x in rows:
                print(x)
            print("- " * 5)
        return "".join(["".join(x) for x in rows])
