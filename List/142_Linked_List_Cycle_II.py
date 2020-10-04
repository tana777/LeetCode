"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Notice that you should not modify the linked list.

Follow up:
Can you solve it using O(1) (i.e. constant) memory?

 

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
 
Constraints:
The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Approach 1 Use additional space to check if there are repeated elements in the node map
"""
Time Complexity: O(n)
Sapce Complexity: O(n)
"""

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        nodeMap = {}
        while head:
            if head in nodeMap:
                return head
            else:
                nodeMap[head] = 1
            head = head.next

# Approach 2: Constant space + slow/fast
# when slow and fast frist met, we keep the fast at this point, and put slow to head position.
# Let slow and fast start to move from their current position and each time, only move one step
# the point where they meet each other is the begin of cycle


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next 
                return slow 

