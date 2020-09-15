
"""
Given the root of a binary tree, return the postorder traversal of its nodes' values.

Follow up: Recursive solution is trivial, could you do it iteratively?

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]
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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.postorderHelp(root, res)
        return res
    def postorderHelp(self, root, res):
        if not root:
            return
        self.postorderHelp(root.left, res)
        self.postorderHelp(root.right, res)
        res.append(root.val)
        

# Approach 2: Iteration
"""
    Time Complexity: O(n)
    Space Complexity: O(n)
"""

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res[::-1]