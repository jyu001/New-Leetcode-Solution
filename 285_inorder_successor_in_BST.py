'''
285. Inorder Successor in BST
DescriptionHintsSubmissionsDiscussSolution
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

Note: If the given node has no in-order successor in the tree, return null.

Example 1:

Input: root = [2,1,3], p = 1

  2
 / \
1   3

Output: 2
Example 2:

Input: root = [5,3,6,2,4,null,null,1], p = 6

      5
     / \
    3   6
   / \
  2   4
 /   
1

Output: null
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        def check(root): # return the smallest number of the tree
            if not root: return None
            if not root.left: return root.val
            else: return check(root.left)
        if not root: return None
        if root.val < p.val: return self.inorderSuccessor(root.right, p)
        elif root.val > p.val: 
            a = self.inorderSuccessor(root.left, p)
            return a if a else root.val
        else: return check(root.right)
        