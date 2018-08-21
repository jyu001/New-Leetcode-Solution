'''
572. Subtree of Another Tree
DescriptionHintsSubmissionsDiscussSolution
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.

'''


class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not t: return True
        if not s: return False
        
        def check(s,t):
            if not t and not s: return True
            elif not t or not s: return False
            if s.val != t.val: return False
            else: return check(s.left,t.left) and check(s.right, t.right)
            
        if check(s,t): return True
        else: 
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)