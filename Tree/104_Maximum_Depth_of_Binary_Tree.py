"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""

# Approach 1: Recursion
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
    
        
# Apporach 2: BFS 
"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        level = 0
        queue = [root]
        while queue:
            for i in range(len(queue)):
                root = queue.pop(0)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            level += 1
        return level
        
# Apporach 2: DFS Iteration
"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = 0
        stack = [(root,1)]
        while stack:
            node, depth = stack.pop()
            if depth > ans:
                ans = depth
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return ans
        
        
        
        
        



