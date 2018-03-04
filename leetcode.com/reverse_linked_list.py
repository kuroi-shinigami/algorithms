#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        _prev = None
        _next = None
        while cur:
            _next = cur.next
            cur.next = _prev
            _prev = cur
            cur = _next
        return _prev
