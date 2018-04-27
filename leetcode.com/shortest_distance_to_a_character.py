#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        targets = [i for i, ch in enumerate(S) if ch == C]
        # print(targets)
        res = []
        next = targets.pop(0)
        prev = next
        for i in range(len(S)):
            if i < next:
                res.append(min(abs(i-prev), abs(next-i)))
            else:
                if targets:
                    res.append(0)
                    prev = next
                    next = targets.pop(0)
                else:
                    res.append(min(abs(i - prev), abs(next - i)))
        return res
