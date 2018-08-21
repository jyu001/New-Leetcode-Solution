'''
138. Copy List with Random Pointer
DescriptionHintsSubmissionsDiscussSolution
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
'''

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        # notice that the random pointer points to a specific random node
        # all you need to do is to map the whole list and copy how all the random pointer points to
        # it's not really a 'random' pointer that you need to make
        # so the key point is to store all nodes into a dict
        if not head: return None
        dct = {}
        new = RandomListNode(head.label)
        p, q = head, new
        dct[p] = q
        while p.next:
            q.next = RandomListNode(p.next.label)
            dct[p.next] = q.next
            p, q = p.next, q.next
        p, q = head, new
        while p:
            if p.random: q.random = dct[p.random]
            p, q = p.next, q.next
        return new