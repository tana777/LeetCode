"""
    Given a binary tree, determine if it is a valid binary search tree (BST).
    
    Assume a BST is defined as follows:
    - The left subtree of a node contains only nodes with keys less than the node's key.
    - The right subtree of a node contains only nodes with keys greater than the node's key.
    - Both the left and right subtrees must also be binary search trees.
"""

"""
    2
   / \
  1   3

Input: [2,1,3]
Output: true

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

## Method 1 Inorder Traversal -- sorted result
"""
    For a binary tree, if we traverse the tree inorder, then the value list should be in strict ascending order
    since no value of two tree node should be equal.
    In this process, we can compare the previous node's value with the next one's, if prev.value >= next.value, then it's not BST.
"""
"""
    Time Complexity: O(n) iterate over all the node
    Space Complexity: O(h) height of the tree, worst case O(n), on average O(lgn)
"""

# First Version: Inorder Traversal + record the value to a list, then check if it's sorted or not! 
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        nodeList = []
        
        def treeTraversal(root: TreeNode, ls: list):
            if not root:
                return root
            left = treeTraversal(root.left, ls)
            ls.append(root.val)
            right = treeTraversal(root.right, ls)
        
        treeTraversal(root, nodeList)
        
        for i in range(len(nodeList)-1):
            if nodeList[i+1] <= nodeList[i]:
                return False
        return True

class Solution:
    def __init__(self, prev):
        self.prev = None

    def isValidBST(self, root: TreeNode) -> bool:
        return self.validCheck(root)

    def validCheck(self, root):
        if not root:
            return True
        if not self.validCheck(root.left):
            return False
        if self.prev and self.prev.val >= root.val:
            return False
        self.prev = root
        return self.validCheck(root.right)


## Method 2: definition


# Wrong but still a good process pass 70/75 cases
# cannot control the tree of its subtree 
    5
   / \
  1   4
     / \
    3   6
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        if root.left and root.val <= root.left.val:
            return False 
        if root.right and root.val >= root.right.val:
            return False 
        return self.isValidBST(root.left) and self.isValidBST(root.right)

# introduce bound
"""
                    root
                    val: a in (-inf, +inf)
   L in (-inf, a)   / \   R in (a, +inf)
            L < a  /   \  R > a 
                   L     R
upper bound of left tree is a 
lower bound of right tree is a 
"""
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.validCheck(root)
    
    def validCheck(self, root, lower=None, upper=None):
        if not root:
            return True
        if (upper or upper==0) and root.val >= upper:
            return False
        if (lower or lower==0) and root.val <= lower:
            return False
        return self.validCheck(root.left, lower, root.val) and \
        self.validCheck(root.right, root.val, upper)

## lower and upper should be numbers, so using float type here

"""
    Time Complexity: O(n)
    Space Complexity: O(h) recursion call stack

"""

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.validCheck(root)
    
    def validCheck(self, root, lower=float('-inf'), upper=float('inf')):
        if not root:
            return True
        if root.val >= upper or root.val <= lower:
            return False
        return self.validCheck(root.left, lower, root.val) and self.validCheck(root.right, root.val, upper)

            
            
     
        