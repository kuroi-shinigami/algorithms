#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Maybe, using lists will be too slow.
        if not strs:
            return ''
        if '' in set(strs):
            return ''
        lengths = [len(x) for x in strs]
        shortest = min(lengths)
        i = lengths.index(shortest)
        lengths.pop()
        if not lengths:
            return strs[i]
        second_shortest = min(lengths)
        lengths.insert(i, shortest)
        second_shortest = strs[lengths.index(second_shortest)]
        shortest = strs[i]
        # 1. Searching for the longest subsequence between two shortest strings
        i = 0
        for x, y in zip(shortest, second_shortest):
            if x != y:
                break
            i += 1
        target_to_check = shortest[:i]
        # 2. This substring may be not common between all suggested strings.
        # Even so, we somehow optimized search length
        while True:
            for x in strs:
                if not x.startswith(target_to_check):
                    # ToDo: decrease length of target string
                    target_to_check = target_to_check[:len(target_to_check)-1]
                    break
            else:
                print(target_to_check)
                break
        return target_to_check
