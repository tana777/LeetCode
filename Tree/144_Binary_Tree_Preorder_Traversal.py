
"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach 1: Recursion
"""
    Time Complexity: O(n)  because the recursive function is T(n) =2⋅T(n/2)+1.
    Space Complexity: O(h) recursion stack depens on the height of the tree
"""
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.preorderHelp(root, result)
        return result
    
    def preorderHelp(self, root, result):
        if not root:
            return
        result.append(root.val)
        self.preorderHelp(root.left, result)
        self.preorderHelp(root.right, result)
        

# Approach 2: Iteration
"""
    Time Complexity: O(n)
    Space Complexity: O(n)
"""
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res