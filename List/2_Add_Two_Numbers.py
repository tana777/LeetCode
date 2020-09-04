"""
    You are given two non-empty linked lists representing two non-negative integers. 
    
    The digits are stored in reverse order and each of their nodes contain a single digit. 
    
    Add the two numbers and return it as a linked list. 
    
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    
    Example:

    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Method 1 
""" Iterate over two Linked list and put the value into two list
    Recover two integers and add them together
    Create a brand new Linked list using the value from the sum in reverse order
    
    Very redundant and use much additional space, but it works! Let us improve it step by step. 

    Time complexity: O(max(n, m))
    Space complexity: O(max(n, m))
"""
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        value1 = []
        value2 = []
        while l1:
            value1.append(l1.val)
            l1 = l1.next
        while l2:
            value2.append(l2.val)
            l2 = l2.next
        res1 = 0
        for i in range(len(value1), 0, -1):
            res1 = res1 + value1.pop() * pow(10,i-1)
        res2 = 0
        for i in range(len(value2), 0, -1):
            res2 = res2 + value2.pop() * pow(10,i-1)
        sumRes = str(res1 + res2)
        sumNode = ListNode(0, None)
        res = sumNode
        for num in sumRes[::-1]:
            sumNode.next = ListNode(int(num), None)
            sumNode = sumNode.next
        return res.next


# Method 2
""" Use two layers to control the addition process
    when one of the Linked list is not done yet, we continue the loop
    the inner part deals with the details of each situation

    create a dummy head/ sentinal node
    addition simulation: over ten 10 we should carry to next node value 
    if sum > 10: value = sum % 10, ct = 1
    else: value = sum, ct = 0

    Here, we ignore one condition inside the loop, when l1 and l2 both come to the end, 
    but the sum is greater than 10, we should add ct to the end.
"""
""" special cases:
    1. two list have different length
    l1: 916 l2:0
    2. sum has more digits
    l1: 18 l2 91 81 + 19 = 100
"""



class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sumNode = ListNode(0, None)
        res = sumNode
        ct = 0
        while l1 or l2:
            if l1 and l2:
                sumVal = l1.val + l2.val + ct
                l1 = l1.next
                l2 = l2.next
            elif not l1:
                sumVal = l2.val + ct
                l2 = l2.next
            else:
                sumVal = l1.val + ct
                l1 = l1.next
            
            if sumVal >= 10:
                sumNode.next = ListNode(mod(sumVal, 10), None)
                ct = 1
            else:
                sumNode.next = ListNode(sumVal, None)
                ct = 0
            sumNode = sumNode.next
        if ct == 1:
            sumNode.next = ListNode(1, None)
        return res.next


## Improvement

"""
    Time Complexity: O(max(m, n)) depends on longest length
    Space Complexity: O(max(m, n)) create a Linkedlist
    if we only need to print each digit of the integer, then this can reduce to constant space
"""

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sumNode = ListNode(0, None)
        res = sumNode
        ct = 0
        while l1 or l2 or ct:
            if l1 and l2:
                sumVal = l1.val + l2.val + ct
                l1 = l1.next
                l2 = l2.next
            elif not l1 and not l2:
                sumVal = ct
            elif not l1:
                sumVal = l2.val + ct
                l2 = l2.next
            else:
                sumVal = l1.val + ct
                l1 = l1.next
            
            if sumVal >= 10:
                sumNode.next = ListNode(sumVal % 10, None)
                ct = 1
            else:
                sumNode.next = ListNode(sumVal, None)
                ct = 0
            sumNode = sumNode.next
        return res.next    

## Improvement -- neat code

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sentinal = sumNode = ListNode(0)
        ct = 0
        while l1 or l2 or ct:
            sumVal = (l1.val if l1 else 0) + (l2.val if l2 else 0) + ct
            if sumVal >= 10:
                sumNode.next = ListNode(sumVal % 10)
                ct = 1
            else:
                sumNode.next = ListNode(sumVal)
                ct = 0
            sumNode = sumNode.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return sentinal.next   


## Further clean and neat code

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sentinal = tail = ListNode(0)
        ct = 0
        while l1 or l2 or ct:
            ct += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            tail.next = ListNode(ct % 10)
            tail = tail.next
            ct //= 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return sentinal.next


l1 = ListNode(1)
l1.next = ListNode(8)
l2 = ListNode(9)
l2.next = ListNode(1)

mysolution = Solution()
sumNode = mysolution.addTwoNumbers(l1, l2)
