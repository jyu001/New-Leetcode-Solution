'''
124. Binary Tree Maximum Path Sum
DescriptionHintsSubmissionsDiscussSolution
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        def check(root):
            # two values: 1st: left/right + root; 2nd: left+root+right
            if not root.left and not root.right:
                return [root.val, root.val]
            elif not root.left:
                b = check(root.right)
                return [max(b[0] + root.val, root.val), max(b[1], root.val, root.val+b[0])]
            elif not root.right:
                a = check(root.left)
                return [max(a[0] + root.val, root.val), max(a[1], root.val, root.val+a[0])]
            else:
                a,b = check(root.left), check(root.right)
                return [max(a[0]+root.val, b[0]+root.val, root.val) , max(a[1], b[1], root.val, root.val+b[0], root.val+a[0], a[0]+root.val+b[0])]
        l = check(root)
        return l[1]