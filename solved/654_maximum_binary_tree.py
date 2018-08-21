'''
654. Maximum Binary Tree
DescriptionHintsSubmissionsDiscussSolution
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1
Note:
The size of the given array will be in the range [1,1000].

'''

class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums: return None
        n = max(nums)
        root = TreeNode(n)
        for i in range(len(nums)):
            if nums[i] == n:
                root.left = self.constructMaximumBinaryTree(nums[:i])
                root.right = self.constructMaximumBinaryTree(nums[i+1:])
        return root