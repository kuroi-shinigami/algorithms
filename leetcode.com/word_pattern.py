#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        keys = {k: None for k in set(pattern)}
        items = str.split()
        if len(items) != len(pattern):
            return False
        for i in range(len(pattern)):
            s = pattern[i]
            if keys[s] is None:
                print(items, str)
                if items[i] not in keys.values():
                    keys[s] = items[i]
                else:
                    return False
            else:
                if keys[s] != items[i]:
                    return False
        return True
