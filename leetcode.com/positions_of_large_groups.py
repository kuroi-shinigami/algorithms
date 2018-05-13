#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        res = []
        counter = 1
        for i in range(1, len(S)):
            if S[i-1] == S[i]:  # seems to be a group
                counter += 1
            else:  # seq is broken
                if counter < 3:
                    counter = 1
                else:
                    res.append([i-counter, i-1])
                    counter = 1
        if counter >= 3:
            res.append([i + 1 - counter, i])
        return res
