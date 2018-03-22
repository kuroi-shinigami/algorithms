#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # =/
        #
        # def list_to_nodes(some_list):
        #     if not some_list:
        #         return
        #     # print("Here!", some_list)
        #     some_list.reverse()
        #     tail = ListNode(some_list.pop(0))
        #     tail.next = None
        #     head = tail
        #     while some_list:
        #         head = ListNode(some_list.pop(0))
        #         head.next = tail
        #         tail = head
        #     h = head
        #     while h:
        #         # print(h.val, end=" ")
        #         h = h.next
        #     print()
        #     return head
        #
        # _head = head
        # _seen = set()
        # while _head:
        #     _seen.add(_head.val)
        #     _head = _head.next
        # # print(_seen, list(sorted(_seen)))
        # return list_to_nodes(list(sorted(_seen)))

        h = head
        while h and h.next:
            if h.val == h.next.val:
                h.next = h.next.next
            else:
                h = h.next
        return head
