"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Use binary search tree's property, for a sorted array, the middle of the array will be the root.
# then for the left subtree, the middle of the left part array will be the new subroot...
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return
        return self.constructBST(nums)
    
    def constructBST(self, nums):
        if len(nums) < 1:
            return 
        mid = len(nums)//2
        node = TreeNode(nums[mid])
        node.left = self.constructBST(nums[:mid])
        node.right = self.constructBST(nums[mid+1:])
        return node