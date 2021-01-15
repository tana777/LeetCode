"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

 

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

 

Constraints:

The number of elements of the BST is between 1 to 10^4.
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Time Complexity: O(n)
Sapce Complexity: O(n) 
"""
# Approach: Inorder traversal + Recursion
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res = [0, 0]
        self.inorder(root, res, k)
        return res[1]
    
    def inorder(self, root, res, k):
        if not root:
            return
        self.inorder(root.left, res, k)
        res[0] += 1
        if res[0] == k:
            res[1] = root.val
        self.inorder(root.right, res, k)


             
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.kth = 0
        self.element = None
        self.inorderTraversal(root, k)
        return self.element
        
    def inorderTraversal(self, root, k):
        if not root:
            return 
        self.inorderTraversal(root.left, k)
        self.kth += 1
        if self.kth == k:
            self.element = root.val
        self.inorderTraversal(root.right, k)
        
## Approach: Stack + Iteration

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        res = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res[k-1]