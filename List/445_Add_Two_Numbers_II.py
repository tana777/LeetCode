"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Use two stack to restore the node value in two Linked lists
Sum them up and form a new Linked list
"""

"""
Time Complexity: O(l1+l2)
Space Complexity: O(max(l1,l2))
"""
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ls1 = []
        while l1:
            ls1.append(l1.val)
            l1 = l1.next
        ls2 = []
        while l2:
            ls2.append(l2.val)
            l2 = l2.next
        ct = 0
        sentinal = None
        while ls1 or ls2 or ct:
            if ls1 and ls2:
                res = ls1.pop() + ls2.pop() + ct
            elif ls1:
                res = ls1.pop() + ct
            elif ls2:
                res = ls2.pop() + ct
            else:
                res = ct
            if res // 10 > 0:
                node = ListNode(res%10)
                ct = 1
            else:
                node = ListNode(res)
                ct = 0
            node.next = sentinal
            sentinal = node

        return sentinal