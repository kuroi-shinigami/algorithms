#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        # Correct again, but not fast enough
        # length = len(s)
        # for sublength in range(length, 0, -1):
        #     half = int(sublength / 2)
        #     for i in range(length - sublength + 1):
        #         for ix in range(half):
        #             if s[i+ix] != s[i + sublength - (ix + 1)]:
        #                 break
        #         else:
        #             return s[i:i + sublength]

        def is_palindrome(x):
            """
            :type x: str
            :rtype: bool
            """
            for i in range(int(len(x) / 2)):
                if x[i] != x[-(i + 1)]:
                    return False
            return True
        if is_palindrome(s):
            return s
        longest = s[0]
        # uneven
        n = len(s)
        for i, ch in enumerate(s):
            if i == 0 or i == n:
                pass
            else:
                left = i - 1
                right = i + 1
                _s = s[left:right]
                # ToDo: if is_palindrome(_s) -> while s[left] == s[right]
                while is_palindrome(_s):
                    if len(_s) > len(longest):
                        longest = _s
                    left -= 1
                    right += 1
                    if left < 0 or right > n:
                        break
                    _s = s[left:right]
        # even
        for i, ch in enumerate(s):
            if i == 0 or i >= n - 1:
                pass
            else:
                left = i - 1
                right = i + 2
                _s = s[left:right]
                while is_palindrome(_s):
                    if len(_s) > len(longest):
                        longest = _s
                    left -= 1
                    right += 1
                    if left < 0 or right > n:
                        break
                    _s = s[left:right]

        return longest

