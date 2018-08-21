'''
83. Remove Duplicates from Sorted List
DescriptionHintsSubmissionsDiscussSolution
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

'''

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
        curr = ListNode(0)
        curr = head
        while curr != None:
            if curr.next==None: break
            elif curr.next.val == curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head