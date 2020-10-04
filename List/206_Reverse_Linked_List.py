"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

# Approach: Iteration (set up prev, curr, nxt node and iterate over the list, and in the end,
# prev pointer would sit at the head of new list. Return prev should be good then.)
"""
1st update:
NULL <- 1    2->3->4->5->NULL
      prev   curr

2nd update:
NULL <- 1 <- 2    3->4->5->NULL
            prev   curr 

Finally:
NULL <- 1 <- 2 <- 3 <- 4 <- 5
                            prev
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        nxt = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
        
# Approach: Recursion

        
