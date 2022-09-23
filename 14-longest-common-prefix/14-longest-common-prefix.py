class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.endOfWord = True
        
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        
        trie = Trie()
        
        for word in strs:
            trie.insert(word)
        
            
        node = trie.root
        ans = ''
        while node:
            if len(node.children) > 1 or node.endOfWord:
                return ans
            
            key = list(node.children)[0]
            ans += key
            
            node = node.children[key]
        return ans