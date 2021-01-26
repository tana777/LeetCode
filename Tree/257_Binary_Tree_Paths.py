"""
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        if not root:
            return res
        self.preorderTraversal(root, res, '')
        return res
    
    def preorderTraversal(self, root, res, path):
        if not root:
            return
        path += str(root.val)
        path += '->'
        if root and not root.left and not root.right:
            path = path[:len(path)-2]
            res.append(path)
            path = path[:len(path)-2]
        self.preorderTraversal(root.left, res, path)
        self.preorderTraversal(root.right, res, path)
        path = path[:len(path)-2]
            
            
        
            
        