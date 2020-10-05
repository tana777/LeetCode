"""
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.

 
Example 1:


Input: [1,1,1,1,1,null,1]
Output: true
Example 2:


Input: [2,2,2,5,2]
Output: false
 

Note:

The number of nodes in the given tree will be in the range [1, 100].
Each node's value will be an integer in the range [0, 99].

"""

# Approach 1: BFS iteration
"""
Time Complexity: O(n)
Space Complexity: O(n)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = [root]
        res = set()
        while queue:
            node = queue.pop(0)
            res.add(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return len(res) == 1

# Improvement: use constant space to store the previous node, and compare if it is the same value as current node
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        self.prev = None
        queue = [root]
        while queue:
            node = queue.pop(0)   
            if self.prev:
                if node.val != self.prev.val:
                    return False
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            self.prev = node
        return True
        

# Approach 2: Recursion 
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        self.prev = None
        return self.univalCheck(root)
    
    def univalCheck(self, root):
        if not root:
            return True
        if self.prev and self.prev.val != root.val:
            return False
        self.prev = root
        return self.univalCheck(root.left) and self.univalCheck(root.right)
        

# Approach 3: DFS Iteration
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = [root]
        prev = None
        while stack:
            node = stack.pop()
            if prev and prev.val != node.val:
                return False
            prev = node
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return True
        