'''
199. Binary Tree Right Side View
DescriptionHintsSubmissionsDiscussSolution
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        l, r = self.rightSideView(root.left), self.rightSideView(root.right)
        if len(l) <= len(r): return [root.val] + r
        else: return [root.val] + r + l[len(r):]