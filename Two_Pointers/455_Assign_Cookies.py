"""
Assume you are an awesome parent and want to give your children some cookies. 
But, you should give each child at most one cookie. Each child i has a greed factor gi, which is the minimum size of a cookie that the child will be content with; and each cookie j has a size sj. 
If sj >= gi, we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

Note:
You may assume the greed factor is always positive.
You cannot assign more than one cookie to one child.
Example 1:
Input: [1,2,3], [1,1]
Output: 1

Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.

Example 2:
Input: [1,2], [1,2,3]
Output: 2
Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
You have 3 cookies and their sizes are big enough to gratify all of the children, 
You need to output 2.
"""

# Approach: Greedy + Two Pointers
"""
sort two lists first, and this dominates the time complexity.
then iterate over children's greed list, for each child, check cookie size and find the appropriate one.
for next child, start going through the cookie size from the current index of list s. 
so overall, it's O(m) + o(n) instead of O(m) * O(n).
"""

"""
    Time Complexity: O(logm + nlogn)
    Space Complexity: O(1)
"""
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ans = 0
        g.sort() # O(mlog(m))
        s.sort() # O(nlog(n))
        cookie = 0
        for child in g: #O(m) + O(n)
            while cookie < len(s) and s[cookie] < child:
                cookie += 1
            if cookie < len(s):
                ans += 1
                cookie += 1
        return ans
            
        
        
