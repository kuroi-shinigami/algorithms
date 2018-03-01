#!/usr/bin/env python


class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        _ROTATES_TO_SELF = {"0", "1", "8"}
        _ROTATES_TO_OTHER = {"2", "5", "6", "9"}
        _ROTATIONS = _ROTATES_TO_SELF | _ROTATES_TO_OTHER
        res = 0
        for n in range(1, N+1):
            # print(f"Cheking {n}")
            _rotates_flag = False
            for d in str(n):
                if d not in _ROTATIONS:
                    break
                if d in _ROTATES_TO_OTHER:
                    _rotates_flag = True
            else:
                if _rotates_flag:
                    # print(f"Adding... {n}")
                    res += 1
        return res

