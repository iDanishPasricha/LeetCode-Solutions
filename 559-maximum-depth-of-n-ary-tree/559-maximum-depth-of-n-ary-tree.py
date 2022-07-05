"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        q= deque();
        q.append(root);
        levels=0;
        if not root: return 0
        while q:
            for i in range(len(q)):
                curr = q.popleft()
                if curr.children:
                    for child in curr.children:
                        q.append(child)
            levels+=1;
        return levels
                
        
        