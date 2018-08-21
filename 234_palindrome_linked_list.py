'''
234. Palindrome Linked List
DescriptionHintsSubmissionsDiscussSolution
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None: return True
        new = ListNode(0)
        new.next = head
        count = 0
        while new.next:
            new.next = new.next.next
            count += 1
        if count == 1: return True
        new.next = head
        for i in range(count//2):
            if i == count//2-1: new.next.next, new.next = None, new.next.next
            else: new.next= new.next.next
        if count%2: new.next =new.next.next # find the starting node of 2nd half
            
        def reverseList(hd):
            """
            :type head: ListNode
            :rtype: ListNode
            """
            if hd == None: return None
            new = ListNode(0)
            new.next = hd.next
            hd.next = None
            while new.next:
                hd, new.next.next = new.next.next, hd
                hd, new.next = new.next, hd
            new.next = hd
            return new.next
        
        new.next = reverseList(new.next)
        
        
        for i in range(count//2):
            if new.next.val - head.val: return False
            new.next, head = new.next.next, head.next
        return True
        
        
        
        