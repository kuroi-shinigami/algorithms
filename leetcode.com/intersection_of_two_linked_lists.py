#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # print("Here!")
        if not (headA and headB):
            # print("nop")
            return
        length_a = 0
        length_b = 0
        h = headA
        while h:
            length_a += 1
            h = h.next
        h = headB
        while h:
            length_b += 1
            h = h.next

        long, short = (headA, headB) if length_a > length_b else (headB, headA)
        diff = abs(length_b - length_a)
        # print("Long: {}".format(long.val))
        # print("Short: {}".format(short.val))
        for i in range(diff):
            long = long.next
        # print(long.val)
        # print(long.next)
        while long or short:
            if long.val == short.val:
                return long
            long = long.next
            short = short.next
        return None
