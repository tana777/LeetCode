"""
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

 

Example 1:

Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".
Example 2:

Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation:
We can turn the last wheel in reverse to move from "0000" -> "0009".
Example 3:

Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation:
We can't reach the target without getting stuck.
Example 4:

Input: deadends = ["0000"], target = "8888"
Output: -1
 

Constraints:

1 <= deadends.length <= 500
deadends[i].length == 4
target.length == 4
target will not be in the list deadends.
target and deadends[i] consist of digits only.
"""

# Approach: BFS
"""
0000 - len:4
Time Complexity: O(10000*8)
Space Complexity: O(10000 + D) D:deadends
"""
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        ## Transform to set which makes accessing faster
        deadends = set(deadends)
        start = '0000'
        ## Dealing with special case
        if start in deadends:
            return -1
        if target == start:
            return 0
        ## Initialize BFS queue
        queue = []
        queue.append(start)
        ## Initialize visited dictionary to avoid going back
        visited = {}
        visited[start] = True
        ## Initialize level/step  
        step = 0
        
        while queue:
            ## BFS its neighbors
            size = len(queue)
            for i in range(size):
                code = queue.pop(0)
                ## check if we find the target
                if code == target:
                    return step
                ## check if we would be locked
                if code in deadends:
                    continue
                ## Collect neighbors/candidates 
                candidates = self.returnAllCode(code)
                for c in candidates:
                    if c not in visited:
                        queue.append(c)
                        visited[c] = True
            step += 1
        return -1
                    
    def returnAllCode(self, code):
        res = []
        for i in range(4):
            res.append(self.turnUp(code, i))
            res.append(self.turnDown(code, i))
        return res
            
    def turnUp(self, code, i):
        item = list(code)
        if item[i] == '9':
            item[i] = '0'
        else:
            item[i] = str(int(item[i]) + 1)
        return ''.join(item)
        
    def turnDown(self, code, i):
        item = list(code)
        if item[i] == '0':
            item[i] = '9'
        else:
            item[i] = str(int(item[i]) - 1)
        return ''.join(item)

        
            
            
        
                
                
                
        
        