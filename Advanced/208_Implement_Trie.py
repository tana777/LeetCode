"""
Implement a trie with insert, search, and startsWith methods.

Example:
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true

Note:
You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""


# Approach 1: use DataIndexedCharMap, i.e. an array of all possible child links.
"""
    Time Complexity: O(l) l is the length of word
    Space Complexity: O(prefixes)
                      O(n*l^2)
"""

class Trie:
    class TrieNode(object):
        def __init__(self):
            self.isKey = False
            self.next = [None] * 26

    def __init__(self):
        self.root = Trie.TrieNode()

    def insert(self, word: str) -> None:
        ptr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not ptr.next[index]:
                ptr.next[index] = Trie.TrieNode()
            ptr = ptr.next[index]
        ptr.isKey = True
        

    def search(self, word: str) -> bool:
        ptr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not ptr.next[index]:
                return False
            else:
                ptr = ptr.next[index]
        return ptr.isKey
    
        

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if not ptr.next[index]:
                return False
            else:
                ptr = ptr.next[index]
        return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


# Approach 2: Use hashtable/dictionary
class Trie:

    def __init__(self):
        self.root = {}
        

    def insert(self, word: str) -> None:
        ptr = self.root
        for c in word:
            if c not in ptr:
                ptr[c] = {}
            ptr = ptr[c]
        ptr['#'] = True


    def search(self, word: str) -> bool:
        ptr = self.root
        for c in word:
            if c not in ptr:
                return False
            ptr = ptr[c]
        return '#' in ptr
 

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        for c in prefix:
            if c not in ptr:
                return False
            ptr = ptr[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)