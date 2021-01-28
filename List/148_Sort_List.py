"""
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105

"""


# Approach 1: Merge sort (top donw) with recursion, so this is not constant space. It's O(logn) call stack.
# KTA: how to find the middle point of a linked list: use slow and fast ptr


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        return self.mergeSort(head)
        
    def mergeSort(self, head):
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        left = self.mergeSort(head)
        right = self.mergeSort(mid)
        return self.merge(left, right)
    
    def merge(self, left, right):
        sentinal = ListNode(0)
        root = sentinal
        while left and right:
            if left.val < right.val:
                root.next = left
                left = left.next
            else:
                root.next = right
                right = right.next
            root = root.next
        if left:
            root.next = left
        if right:
            root.next = right
        return sentinal.next
                
# Approach 2: Merge sort (bottom up) to achieve constant space
    