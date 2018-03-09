from unittest import TestCase

from reverse_linked_list import Solution

s = Solution()


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def list_to_nodes(some_list):
    if not some_list:
        return
    print(some_list)
    some_list.reverse()
    tail = ListNode(some_list.pop(0))
    tail.next = None
    head = tail  # BUG: head = None causes empty list instead 1-noded
    while some_list:
        head = ListNode(some_list.pop(0))
        head.next = tail
        tail = head
    h = head
    while h:
        print(h.val, end=" ")
        h = h.next
    print()
    return head


class TestSolution(TestCase):
    """"""

    def test_0(self):
        obj1 = s.reverseList(list_to_nodes([1, 2, 3, 4]))
        self.assertEqual(obj1.val, 4)
        self.assertEqual(obj1.next.val, 3)
