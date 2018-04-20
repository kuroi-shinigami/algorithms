#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        # ToDo: find more tricky way with counting indices and checking dots?

        for view in [board, zip(*board)]:
            for line in view:
                print(line)
                digits = [x for x in line if x != '.']
                if len(digits) != len(set(digits)):
                    return False

        for x, y in {(0, 0), (3, 0), (6, 0), (0, 3), (0, 6), (3, 3), (3, 6), (6, 3), (6, 6)}:
            seen = set()
            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    if board[i][j] != '.':
                        if board[i][j] in seen:
                            return False
                        else:
                            seen.add(board[i][j])
        return True
