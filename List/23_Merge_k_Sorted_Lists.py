"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists or len(lists)==0:
            return None
        nodeVal = []
        for node in lists:
            while node:
                nodeVal.append(node.val)
                node = node.next
        sentinal = root = ListNode(0)
        nodeVal.sort()
        for val in nodeVal:
            root.next = ListNode(val) 
            root = root.next
        return sentinal.next
                

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        return self.mergeSort(lists)
    
    def mergeSort(self, lists):
        if len(lists) <= 1:
            return lists[0]
        mid = len(lists)//2
        left = self.mergeSort(lists[:mid])
        right = self.mergeSort(lists[mid:])
        return self.merge(left, right)
        

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
            
        
        