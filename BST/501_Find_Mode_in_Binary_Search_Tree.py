"""

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(n)
# Space Complexity: O(n)
# Use a dictionary to store the count of each element
# first loop to find the mode count
# second loop to add all modes into result list
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        mode = {}
        self.prev = TreeNode(float('-inf'))
        self.inorderTraversal(root, mode)
        mode_count = 0
        res = []
        for key, val in mode.items():
            if val > mode_count:
                mode_count = val
        for key, val in mode.items():
            if val == mode_count:
                res.append(key)
        return res
                
    def inorderTraversal(self, root, mode):
        if not root:
            return
        self.inorderTraversal(root.left, mode)
        if root.val not in mode:
            mode[root.val] = 1
        if self.prev.val == root.val:
            mode[self.prev.val] += 1
        self.prev = root
        self.inorderTraversal(root.right, mode)
        


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# first inorder traversal to record the count of mode
# second traversal to collect mode
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        self.prevVal = 0
        self.currCount = 0
        self.maxCount = 0
        self.modeCount = float('inf')
        self.res = []
        self.inorder(root)
        self.modeCount = self.maxCount
        self.currCount = 0
        self.inorder(root)
        return self.res
        
    def computeMode(self, val):
        if self.prevVal == val and self.currCount > 0:
            print(self.prevVal)
            self.currCount += 1
        else:
            self.prevVal = val
            self.currCount = 1

        if self.currCount > self.maxCount:
            self.maxCount = self.currCount
            
        if self.currCount == self.modeCount:
            self.res.append(val)
            

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.computeMode(root.val)
        self.inorder(root.right)
    
            
            