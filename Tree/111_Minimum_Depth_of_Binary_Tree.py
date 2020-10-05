"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""

# Approach 1: Recursion
"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left or not root.right:
            return 1 + max(self.minDepth(root.left), self.minDepth(root.right))
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

# Approach 2: DFS Iteration 
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        ans = float('inf')
        while stack:
            node, depth = stack.pop()
            if not node.left and not node.right:
                ans = min(ans, depth)
            if node.left:
                stack.append((node.left, depth+1))
            if node.right:
                stack.append((node.right, depth+1))
        return ans
        
            
        
