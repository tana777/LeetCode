"""
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. 
For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. 
And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class.
If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. 
And you have to output the total number of friend circles among all the students.

Example 1:

Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.
 

Example 2:

Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
"""

# Method 1 DFS
""" 
    Since everyone is a friend of themselves. We use DFS to find a circle of every student and remove
    their friendship. How many kind of students that we have to restart finding their circles which 
    means how many friend circles in this class. -- find #of connected components
"""

"""
    Time Complexity: O(n^2) worst case: every one has only one friend, themselves. 
    Space Complexity: O(n^2) recursion call stack
"""

class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        if n==0:
            return 0
        ans = 0

        for i in range(n):
            if M[i][i] == 1:
                ans += 1
                self.dfs(M, i, n)
        return ans 

    def dfs(self, M, curr, n):
        for i in range(n):
            if M[curr][i] == 1:
                M[curr][i] = M[i][curr] = 0
                self.dfs(M, i, n)


mySol = Solution()
M = [[1,1,0],
    [1,1,0],
    [0,0,1]]
mySol.findCircleNum(M)