'''
21. Merge Two Sorted Lists
DescriptionHintsSubmissionsDiscussSolution
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        head = res
        while l1 and l2:
            if l1.val<=l2.val:
                res.next = l1
                res, l1 = res.next, l1.next
            else:
                res.next = l2
                res, l2 = res.next, l2.next
        if l1 == None: res.next = l2
        elif l2 == None: res.next = l1
        return head.next