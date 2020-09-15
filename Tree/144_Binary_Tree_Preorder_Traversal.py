
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
        stack = []
        res = []
        node = root
        while node or len(stack) > 0:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return res