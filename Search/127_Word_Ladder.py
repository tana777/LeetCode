"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

"""
# Approach: BFS
"""
Time Complexity: O(n*26^l) -> O(n*26^l/2), l = len(word), n=|wordList|
Space Complexity: O(n)
"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # BFS template
        
        # dealing with edge case
        if beginWord == endWord and beginWord in wordList:
            return 0
        
        # generate all the possible words within one transformation
        all_combo_dict = {}
        n = len(beginWord)
        for w in wordList:
            for idx in range(n):
                if w[:idx] + '*' + w[idx+1:] in all_combo_dict:
                    all_combo_dict[w[:idx] + '*' + w[idx+1:]].append(w)
                else:
                    all_combo_dict[w[:idx] + '*' + w[idx+1:]] = [w]
        
        # initialize queue for BFS
        queue = []
        visited = set()
        queue.append(beginWord)
        visited.add(beginWord)
        
        step = 0
        
        # BFS neighbors
        while queue:
            size = len(queue)
            for i in range(size):
                word = queue.pop(0)
                if word == endWord:
                    return step + 1
                candidates = self.findAllCandidates(word, all_combo_dict)
                for item in candidates:
                    if item not in visited:
                        queue.append(item)
                        visited.add(item)
            step += 1
        return 0
    
    def findAllCandidates(self, word, all_combo_dict):
        result = set()
        n = len(word)
        for i in range(n):
            if word[:i] + '*' + word[i+1:] in all_combo_dict:
                for item in all_combo_dict[word[:i] + '*' + word[i+1:]]:
                    result.add(item)
        return result
                    
                
            
            
        