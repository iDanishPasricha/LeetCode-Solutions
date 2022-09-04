class TrieNode:
    def __init__(self):
        self.children  = {}
        self.endofword = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            
        curr.endofword = True
        

    def search(self, word: str) -> bool:
        
        def dfs(index,root):
            curr = root
            for i in range(index,len(word)):
                char = word[i]
                if char==".": #recursive condition
                    for child in curr.children.values():
                        if dfs(i+1,child):
                            return True
                    return False
    
                else:   #simple iterative condition (no dot)
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
            return curr.endofword 
            
            
        return dfs(0,self.root)
    
    
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)