"""
You are given the root of a binary search tree (BST), where exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

Follow up: A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

 

Example 1:


Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
Example 2:


Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
 

Constraints:

The number of nodes in the tree is in the range [2, 1000].
-231 <= Node.val <= 231 - 1
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res = []
        self.collectNodeValue(root, res)
        res.sort()
        self.reconstructBST(root, res)
        
    def collectNodeValue(self, root, res):
        if not root:
            return
        self.collectNodeValue(root.left, res)
        res.append(root.val)
        self.collectNodeValue(root.right, res)
        
    def reconstructBST(self, root, res):
        if not root:
            return
        self.reconstructBST(root.left, res)
        root.val = res.pop(0)
        self.reconstructBST(root.right, res)
        

# inorder traversal with Recursion to find the problemactic pairs and store them into a list
# according to the number of pairs to determine which kind of swap it took then swap the values 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = TreeNode(float('-inf'))
        candidates = []
        self.inorderTraversal(root, candidates)
        if len(candidates) == 2:
            candidates[0][0].val, candidates[1][1].val = candidates[1][1].val, candidates[0][0].val
        else:
            candidates[0][0].val, candidates[0][1].val = candidates[0][1].val, candidates[0][0].val
        
    def inorderTraversal(self, root, candidates):
        if not root:
            return
        self.inorderTraversal(root.left, candidates)
        if self.prev.val > root.val:
            candidates.append([self.prev, root])
        self.prev = root
        self.inorderTraversal(root.right, candidates)
        
            

# inorder traversal with Iteration
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr, prev, stack, candidates = root, TreeNode(float('-inf')), [], []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if prev.val > curr.val:
                candidates.append([prev, curr])
            prev = curr
            curr = curr.right
        
        if len(candidates) == 1:
            candidates[0][0].val, candidates[0][1].val = candidates[0][1].val, candidates[0][0].val
        else:
            candidates[0][0].val, candidates[1][1].val = candidates[1][1].val, candidates[0][0].val
            
            
            
            