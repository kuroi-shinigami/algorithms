#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        # Too slow and, of course, mutable
        ##################################
        # while matrix:
        #     print(matrix)
        #     try:
        #         diag = set()
        #         for i, l in enumerate(matrix):
        #             diag.add(l.pop(i))
        #             # print(diag)
        #             if len(diag) != 1:
        #                 return False
        #     except IndexError:
        #         matrix = [x for x in matrix if x]
        # return True

        height = len(matrix)
        width = len(matrix[0])
        # we do not need to do anything with bottom-left and top-right corners
        # so for 4x4 we check only 5 diagonals and for 2x9 only 8
        for x in matrix:
            print(x)
        for idx in range(2, height+width-1):
            diag = set()
            counter = idx
            for ic in range(counter):
                ix = height-counter+ic
                if ix >= 0:
                    try:
                        # print("M[{}][{}] = {}".format(height - counter + ic, ic, matrix[height - counter + ic][ic]))
                        diag.add(matrix[ix][ic])
                    except IndexError:
                        pass
                if len(diag) > 1:
                    print(diag)
                    return False

        # ToDo:
        # Another idea: check if common sublists are equal. In example 1 it should be [1, 2] with shift in every row

        return True
