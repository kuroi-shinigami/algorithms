#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        valid = {'L', 'R', 'U', 'D'}
        _moves = {x: 0 for x in valid}
        for x in moves:
            if x not in valid:
                return False
            _moves[x] += 1  # or += ro only two keys?
        if (_moves['D'] == _moves['U']) and (_moves['L'] == _moves['R']):
            return True
        return False
