'''
328. Odd Even Linked List
DescriptionHintsSubmissionsDiscussSolution
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None: return head
        count = 0
        new, h1, t0, t1 = ListNode(0), ListNode(0), ListNode(0), ListNode(0)
        new.next = head
        if new.next == None or new.next.next == None: return head
        if new.next.next:
            t0.next = head
            h1.next, t1.next = new.next.next, new.next.next
            new.next = new.next.next.next
        
        while new.next:
            if count%2==0:
                t0.next.next, t0.next = new.next, new.next
            else:
                t1.next.next, t1.next = new.next, new.next
            new.next = new.next.next
            count += 1
            '''
            k = ListNode(0)
            k.next = head
            while k.next: 
                print(count, k.next.val)
                k.next = k.next.next
            '''
        t0.next.next = h1.next
        t1.next.next = None
        return head