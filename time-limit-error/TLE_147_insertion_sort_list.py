'''
147. Insertion Sort List
DescriptionHintsSubmissionsDiscussSolution
Sort a linked list using insertion sort.


A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
 

Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None: return None
        
        new= ListNode(0)
        new.next = head
        
        def check(i, m):
            #print (i, m)
            curr, ist, insertion = new, ListNode(m), False
            for j in range(i): 
                if curr.next.val>m and insertion==False:
                    ist.next, curr.next = curr.next, ist
                    insertion = True
                    curr = curr.next
                curr = curr.next
            if insertion: curr.next, curr = curr.next.next, curr.next.next
            # curr.next, curr = curr.next.next, curr.next # this is wrong, be careful
            else: curr = curr.next.next
            if curr: check(i+1, curr.val)
                
        if head.next: check(1, head.next.val)
        
        return new.next
                        