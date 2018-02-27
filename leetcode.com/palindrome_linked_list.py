#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        h = head
        res = []
        while h:
            res.append(h.val)
            h = h.next
        n = len(res)
        for i in range(int(n/2)):
            if res[i] != res[n - i - 1]:
                return False
        return True

