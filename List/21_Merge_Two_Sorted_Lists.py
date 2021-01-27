"""
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

 

Example 1:


Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.merge(l1,l2)
        
        
    def merge(self, l1, l2):
        if not l1 and not l2:
            return l1
        if not l1 or not l2:
            return l1 if l1 else l2
        sentinal = root = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                root.next = l1
                l1 = l1.next
            else:
                root.next = l2
                l2 = l2.next
            root = root.next
        if l1:
            root.next = l1
        if l2:
            root.next = l2
        return sentinal.next
            
            
            
        