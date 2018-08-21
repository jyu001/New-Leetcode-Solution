'''
203. Remove Linked List Elements
DescriptionHintsSubmissionsDiscussSolution
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head and head.val == val: head = head.next
        if not head: return None
        n = ListNode(0)
        n.next = head
        while n.next.val:
            a = n.next.next
            if not a: return head
            elif a.val == val: n.next.next = a.next
            else: n.next = a
        