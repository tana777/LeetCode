"""
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:
1 <= n <= 45
"""

# Approach 1: Simple Recursion: memory intensive 
# Fibonacci Number 
# Time Limit Exceeded since we repeatedly compute the smaller pieces of problems
"""
    Time complexity : O(2^n) Size of recursion tree will be 2^n
    Space complexity: O(n) The depth of the recursion tree can go upto n
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)

# Improve recursion by remember what we already computed before, this is called 
# Recursion with Memoization
"""
In the previous approach, we redundantly compute the result for every step.
Instead, we could store the result at each step in an array. 
Returning the result from the array whenever the function is called again.
In this way, we are pruning recursion tree with the help of this array and 
reducing the size of recursion tree up to n.
"""
class Solution:
    def __init__(self):
        self.memo = {}
        
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        if n in self.memo:
            return self.memo[n]
        self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.memo[n]



# Approach 2: Improve by storing the result for each case which avoids unnecessary computing
"""
    Time Complexity: O(n)
    Sapce Complexity: O(n)
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        res = [0] * (n+1)
        res[0] = 1
        res[1] = 1
        for i in range(2,n+1):
            res[i] = res[i-1] + res[i-2]
        return res[n]

# In previous approach, we create an array to pre-compute the number of steps for 
# each value smaller and euqal to n. There's no need to store the rest of the array,
# so we only use three variables to compute the steps and update them correspondingly.

# f1 = 1 beforetwostep
# f2 = 2 beforeonestep
# f3 = f1 + f2

# f1 = f2
# f2 = f3 
"""
    Time Complexity: O(n)
    Sapce Complexity: O(1)
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        beforeTwo = 1
        beforeOne = 1
        curr = 0
        if n <= 1:
            return beforeOne
        for i in range(2, n+1):
            curr = beforeTwo + beforeOne
            beforeTwo = beforeOne
            beforeOne = curr
        return curr

        

         
        