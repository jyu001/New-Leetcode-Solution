'''
94. Binary Tree Inorder Traversal
DescriptionHintsSubmissionsDiscussSolution
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?


'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None: return []
        res = []
        if root.left: res += self.inorderTraversal(root.left)
        res.append(root.val)
        if root.right: res += self.inorderTraversal(root.right)
        return res