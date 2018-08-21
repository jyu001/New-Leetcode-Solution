'''
92. Reverse Linked List II
DescriptionHintsSubmissionsDiscussSolution
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
'''

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m==n: return head
        newhead, h1, h2, h3 = ListNode(0), ListNode(0), ListNode(0), ListNode(0)
        newhead.next, h1.next, h2.next, h3.next = head, head, head, head
        
        # why? 
        if m==1: h1.next = newhead
        for i in range(m):
            h3.next = h3.next.next
            if i < m-1: h2.next = h2.next.next
            if i < m-2: h1.next = h1.next.next
        for i in range(n-m):
            h2.next.next, h3.next.next, h1.next.next= h3.next.next, h1.next.next, h3.next
            h3.next = h2.next.next
        return newhead.next