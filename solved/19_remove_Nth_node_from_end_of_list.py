'''
19. Remove Nth Node From End of List
DescriptionHintsSubmissionsDiscussSolution
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        new = ListNode(0)
        new.next = head
        head = new
        end = head
        #print(head.val)
        for i in range(n):
            end = end.next    
        curr = head
        while end.next:
            end, curr = end.next, curr.next
        curr.next = curr.next.next
        return head.next
        