'''
143. Reorder List
DescriptionHintsSubmissionsDiscussSolution
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        n = ListNode(0)
        n.next = head
        count = 0
        
        # count number of nodes
        while n.next:
            count += 1
            n.next = n.next.next
        
        # find the start of the 2nd half
        n.next = head
        for i in range((count+1)//2):
            if i == (count+1)//2-1: n.next.next, n.next = None, n.next.next # end of 1st half == None
            else: n.next = n.next.next
        # reverse the 2nd half
        t = ListNode(0)
        t.next = n.next
        if t.next:
            while t.next.next:
                # here notice that, need to define t.next.next.next first, otherwise, error 'nontype has no next'
                n.next, t.next.next.next, t.next.next = t.next.next, n.next, t.next.next.next
        t.next = head
        
        for i in range(count//2):
            t.next.next, n.next.next, t.next, n.next = n.next, t.next.next, t.next.next, n.next.next
        