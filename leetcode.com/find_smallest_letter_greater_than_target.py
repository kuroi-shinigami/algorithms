#!/usr/bin/env python


class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for l in letters:
            if target < l:
                return l
        return letters[0]
