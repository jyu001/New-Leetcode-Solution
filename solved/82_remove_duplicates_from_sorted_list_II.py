'''
82. Remove Duplicates from Sorted List II
DescriptionHintsSubmissionsDiscussSolution
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
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
        if head == None: return None
        h0 = t0 = curr = ListNode(0)
        h0.next = t0.next = head
        curr = head
        while curr:
            curr = curr.next
            if curr == None: break
            if curr.val != t0.next.val:
                t0 = t0.next
                continue
            else:
                while curr.next and curr.val == t0.next.val:
                    curr = curr.next
                if curr.val == t0.next.val: 
                    t0.next = None
                    break
                if h0.next.val==t0.next.val: h0.next = curr
                t0.next = curr
            
        return h0.next