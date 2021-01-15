"""
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:
Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
 
Note:

There are at least two nodes in this BST.
This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach 1: Use BST's property: if we inorder traverse the tree, we can 
# get a sorted array, then we iterate the sorted list, compare the current
# with next value, remember the absolute minimum difference 

""" 
    Time Complexity: O(n)
    Space Complexity: O(n)
"""
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        resList = []
        self.getNodevalue(resList, root)
        minDiff = abs(resList[0] - resList[1])
        for i in range(len(resList)-1):
            if abs(resList[i] - resList[i+1]) < minDiff:
                minDiff = abs(resList[i] - resList[i+1])
        return minDiff
            
            
    def getNodevalue(self, res, root):
        if not root:
            return
        self.getNodevalue(res, root.left)
        res.append(root.val)
        self.getNodevalue(res, root.right)
        
# Improvement: reduce space complexity to O(h), here h is the height of BST, O(logn)
# Instead of store the value to a list, we can use a prev pointer to track previous node
# value and compare with the current node value.

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.prev = None
        self.minDiff = float('inf')
        self.diffHelp(root)
        return self.minDiff
    
    def diffHelp(self, root):
        if not root:
            return
        self.diffHelp(root.left)
        if self.prev is not None:
            self.minDiff = min(self.minDiff, (root.val - self.prev))
        self.prev = root.val
        self.diffHelp(root.right)

class Solution:
    def __init__(self):
        self.prev = None
        self.diff = float('inf')
        
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.inorderTraversal(root)
        return self.diff

        
    def inorderTraversal(self, root):
        if not root:
            return
        self.inorderTraversal(root.left)
        if self.prev:
            if abs(self.prev.val - root.val) < self.diff:
                self.diff = abs(self.prev.val - root.val)
        self.prev = root
        self.inorderTraversal(root.right)
        
        
# Approach 2: Recursion -- bound concept according to the property of BST, 
# like problem 98: Validate Binary Search Tree

"""
    Time Complexity: O(n)
    Space Complexity: O(h) height of the tree
"""

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        return self.minDiff(root, float('-inf'), float('inf'))

    def minDiff(self, root, lo, hi):
        if not root:
            return hi - lo 
        left = self.minDiff(root.left, lo, root.val)
        right = self.minDiff(root.right, root.val, hi)
        return min(left, right)