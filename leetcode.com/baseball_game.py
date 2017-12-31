#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        # Not clever, but it works. Slow, but in-place
        ix = 0
        target = len(ops)
        while ix < target:
            try:
                ops[ix] = int(ops[ix])
            except ValueError:
                if ops[ix] == "C":
                    idx = ops.index("C")
                    ops.pop(idx-1)
                    ops.pop(idx - 1)
                    target -= 2
                    ix -= 2
                elif ops[ix] == "D":
                    idx = ops.index("D")
                    ops[idx] = int(ops[idx - 1]) * 2
                elif ops[ix] == "+":
                    idx = ops.index("+")
                    ops[idx] = int(ops[idx - 1]) + int(ops[idx - 2])
            ix += 1
        return sum(ops)
