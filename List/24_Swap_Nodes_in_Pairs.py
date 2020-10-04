"""
Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.
"""

# Approach: Iteration + we need a sentinal node to make life easier
"""
Time Complexity: O(n)
Space Complexity: o(1)

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        sentinal = ListNode(0)
        sentinal.next = head
        head = sentinal
        while head.next and head.next.next:
            n1 = head.next
            n2 = head.next.next
            head.next = n2
            n1.next = n2.next
            n2.next = n1
            head = n1

        return sentinal.next

        
