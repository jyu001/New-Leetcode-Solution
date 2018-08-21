# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0: return None
        head = ListNode(0)
        head.next = lists[0]
        a = head
        if len(lists) == 1: return a.next
        for b in lists[1:]:
            while a.next and b:
                if (a.next).val > b.val:
                    m = a.next
                    a.next = b
                    a = a.next
                    b = m
                else:
                    a = a.next
            if a.next == None:
                a.next = b
            a = head
        return head.next