"""
Given the root node of a binary search tree (BST) and a value. 
You need to find the node in the BST that the node's value equals the given value. 
Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

For example, 

Given the tree:
        4
       / \
      2   7
     / \
    1   3

And the value to search: 2
You should return this subtree:

      2     
     / \   
    1   3
In the example above, if we want to search the value 5, since there is no node with value 5, 
we should return NULL.

Note that an empty tree is represented by NULL, therefore you would see the expected output 
(serialized tree format) as [], not null
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach: Recursion
"""
    Time Complexity: O(logn ~ n)
    Space Complexity: O(logn ~ n)
"""
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        return self.searchHelp(root, val)
    
    def searchHelp(self, root, val):
        if not root:
            return None
        if root.val == val:
            return root
        if root.val > val:
            return self.searchHelp(root.left, val)
        else:
            return self.searchHelp(root.right, val)

        
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        self.res = None
        self.searchHelper(root, val)
        return self.res
    
    def searchHelper(self, root, val):
        if not root:
            return
        self.searchHelper(root.left, val)
        if root.val == val:
            self.res = root
        self.searchHelper(root.right, val)