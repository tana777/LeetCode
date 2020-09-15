
"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.inorderHelper(root, result)
        return result
    
    def inorderHelper(self, root, result):
        if not root:
            return
        self.inorderHelper(root.left, result)
        result.append(root.val)
        self.inorderHelper(root.right,result)
        


# Approach 2: Iteration
"""
    Time Complexity: O(n)
    Space Complexity: O(n)
"""

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        result = []
        node = root
        while node or len(stack) > 0:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node.val)
            node = node.right
        return result
            
        
        