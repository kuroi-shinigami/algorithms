from unittest import TestCase

from palindrome_linked_list import Solution

s = Solution()


# Definition for singly-linked list.
class ListNode(object):
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
    head = None
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

    def test_1(self):
        self.assertEqual(s.isPalindrome(list_to_nodes([])), True)

    def test_2(self):
        self.assertEqual(s.isPalindrome(list_to_nodes([1, 2, 3, 4, 3, 2, 1])), True)

    def test_3(self):
        self.assertEqual(s.isPalindrome(list_to_nodes([1, 2, 3, 4])), False)

    # def test_(self):
    #     self.assertEqual(s.isPalindrome(), )
